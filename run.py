import logging
import os

from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Log environment setup
api_key = os.getenv("GROQ_API_KEY")
logger.info(f"GROQ_API_KEY present: {bool(api_key)}")

try:
    from ui import demo

    logger.info("Successfully imported UI module")
    demo.launch(show_error=True)
except Exception as e:
    logger.error(f"Error starting application: {str(e)}")
    raise
