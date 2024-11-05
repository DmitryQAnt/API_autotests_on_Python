# Set up basic configuration for logging
import logging


logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def log_request_response(response):
    logger.info(f"Request URL: {response.request.url}")
    logger.info(f"Request method: {response.request.method}")
    logger.info(f"Request headers: {response.request.headers}")
    logger.info(f"Request body: {response.request.body}")
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")
