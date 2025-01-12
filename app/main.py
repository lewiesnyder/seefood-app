import os
import streamlit as st
import logging
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.models.hotdog_classifier import HotdogClassifier
from app.utils.image_utils import process_image, process_image_sync

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="SeeFood API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize classifier
classifier = HotdogClassifier()

@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    """Classify an image as hotdog or not hotdog."""
    logger.debug(f"Received image for classification: {file.filename}")
    try:
        image = await process_image(file)
        logger.debug("Image processed successfully")
        result = classifier.classify(image)
        logger.debug(f"Classification result: {result}")
        return {"is_hotdog": result}
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return {"error": str(e)}, 500

# Streamlit UI
def main():
    st.title("SeeFood - Hotdog Detector")
    st.write("Upload an image to check if it's a hotdog!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        logger.debug(f"File uploaded in Streamlit UI: {uploaded_file.name}")
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Is it a hotdog?"):
            with st.spinner("Analyzing..."):
                try:
                    # Process the image
                    logger.debug("Processing image in Streamlit UI")
                    image = process_image_sync(uploaded_file)
                    logger.debug("Image processed successfully")
                    
                    # Classify the image
                    logger.debug("Classifying image in Streamlit UI")
                    result = classifier.classify(image)
                    logger.debug(f"Classification result: {result}")
                    
                    if result:
                        st.success("Hotdog! 🌭")
                    else:
                        st.error("Not Hotdog! ❌")
                except Exception as e:
                    logger.error(f"Error in Streamlit UI: {str(e)}", exc_info=True)
                    st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main() 