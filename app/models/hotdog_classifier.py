import os
import logging
from dotenv import load_dotenv
import ollama

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

class HotdogClassifier:
    def __init__(self):
        self.base_url = None
        self.model = "llama3.2-vision:latest"
        logger.debug(f"Initialized HotdogClassifier with base_url: {self.base_url}, model: {self.model}")
        
    def classify(self, base64_data: str) -> bool:
        """
        Classify an image as hotdog or not hotdog using Ollama's Vision model.
        Args:
            base64_data: Base64 encoded image data
        Returns:
            bool: True if hotdog, False otherwise
        """
        logger.debug("Starting classification process")
        prompt = 'You are an image classifier. You job is to look at an image a classify it as either "hotdog" or "not hotdog". Do not respond with anything other than "hotdog" or "not hotdog".'
        
        try:
            logger.debug(f"Making request to Ollama with base64 image data of length: {len(base64_data)}")
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                images=[base64_data],
                stream=False
            )
            
            logger.debug(f"Raw response from Ollama: {response}")
            response_text = response.response.lower().strip()
            logger.debug(f"Parsed response text: '{response_text}'")
            
            # Check if the response contains "hotdog" (case insensitive)
            is_hotdog = "hotdog" in response_text and "not" not in response_text
            logger.debug(f"Final classification: {'hotdog' if is_hotdog else 'not hotdog'}")
            
            return is_hotdog
            
        except Exception as e:
            logger.error(f"Error during classification: {str(e)}", exc_info=True)
            return False 