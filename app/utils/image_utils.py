from PIL import Image
import io
import logging
import base64
from fastapi import UploadFile

# Configure logging
logger = logging.getLogger(__name__)

def encode_image(image: Image.Image) -> str:
    """Convert PIL Image to base64 string."""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    return base64.b64encode(img_bytes).decode()

async def process_image(file: UploadFile) -> str:
    """
    Process an uploaded image file and return base64 encoded data.
    """
    logger.debug(f"Processing image: {file.filename}")
    
    # Read the image file
    contents = await file.read()
    logger.debug(f"Read {len(contents)} bytes from file")
    
    # Open and resize the image
    image = Image.open(io.BytesIO(contents))
    logger.debug(f"Original image size: {image.size}, mode: {image.mode}")
    
    # Convert to RGB if necessary
    if image.mode != "RGB":
        logger.debug(f"Converting image from {image.mode} to RGB")
        image = image.convert("RGB")
    
    # Resize to a reasonable size while maintaining aspect ratio
    max_size = (512, 512)
    original_size = image.size
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    logger.debug(f"Resized image from {original_size} to {image.size}")
    
    # Convert to base64
    base64_data = encode_image(image)
    logger.debug(f"Converted image to base64 string of length: {len(base64_data)}")
    
    return base64_data

def process_image_sync(file) -> str:
    """
    Synchronous version of process_image for Streamlit UI.
    """
    logger.debug(f"Processing image synchronously")
    
    # Read the image file
    if isinstance(file, UploadFile):
        contents = file.file.read()
    else:
        contents = file.read()
    logger.debug(f"Read {len(contents)} bytes from file")
    
    # Open and resize the image
    image = Image.open(io.BytesIO(contents))
    logger.debug(f"Original image size: {image.size}, mode: {image.mode}")
    
    # Convert to RGB if necessary
    if image.mode != "RGB":
        logger.debug(f"Converting image from {image.mode} to RGB")
        image = image.convert("RGB")
    
    # Resize to a reasonable size while maintaining aspect ratio
    max_size = (512, 512)
    original_size = image.size
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    logger.debug(f"Resized image from {original_size} to {image.size}")
    
    # Convert to base64
    base64_data = encode_image(image)
    logger.debug(f"Converted image to base64 string of length: {len(base64_data)}")
    
    return base64_data 