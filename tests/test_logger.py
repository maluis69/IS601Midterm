import logging
from calculator.logger import logger
import os

def test_logging_setup():
    # Temporarily set LOG_LEVEL to INFO
    os.environ["LOG_LEVEL"] = "INFO"
    logger.setLevel(logging.INFO)
    
    assert logger.level == logging.INFO
