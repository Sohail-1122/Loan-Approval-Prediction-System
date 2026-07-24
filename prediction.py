import joblib
import numpy as np
from src.logger import logger

logger.info("Loading scaler and model...")

scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/svm_model.pkl")

logger.info("Scaler and model loaded successfully")

def predict_loan(data):

    logger.info(f"Received Input: {data}")

    data = np.array(data).reshape(1, -1)

    scaled_data = scaler.transform(data)

    logger.info("Data scaled successfully")

    prediction = model.predict(scaled_data)

    probability = model.predict_proba(
        scaled_data
    )[0][1]

    logger.info(
        f"Prediction={prediction[0]}, Probability={probability:.2%}"
    )

    return prediction[0], probability