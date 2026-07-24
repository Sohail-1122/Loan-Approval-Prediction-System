import logging
import os

# Create folders
os.makedirs("logs", exist_ok=True)
os.makedirs("models", exist_ok=True)

LOG_FILE = os.path.join("logs", "app.log")

# Create logger
logger = logging.getLogger("LoanPrediction")
logger.setLevel(logging.DEBUG)

# Prevent duplicate logs
if not logger.handlers:

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)