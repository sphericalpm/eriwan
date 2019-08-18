# The top-level that defines the Flask application instance
import logging

from app import app

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        filename="eriwan_podcast.log"
    )
