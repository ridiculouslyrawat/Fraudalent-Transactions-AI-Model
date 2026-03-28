# Fraudalent-Transactions-AI-Model
Real-time Fraud Detection System: An end-to-end ML pipeline using XGBoost and FastAPI to identify fraudulent transactions via a REST API.
Real-Time AI Fraud Detection System
A lightweight, end-to-end machine learning pipeline that trains an XGBoost classifier to identify fraudulent transactions and serves predictions via a high-performance FastAPI REST interface.

Overview

This project demonstrates how to move from raw data to a live AI service. It consists of three main components:

Trainer (train.py): Generates synthetic transaction data and trains an XGBoost model.

API Server (main.py): A FastAPI-based service that loads the trained model and provides a /predict endpoint.

Client Tester (test_fraud.py): An interactive terminal-based tool to send transaction data to the server and receive instant analysis.

Technical Stack
Logic: Python 3.x

Machine Learning: XGBoost, Scikit-Learn (StandardScaler)

API Framework: FastAPI & Uvicorn (ASGI server)

Data Handling: Pandas & NumPy

Serialization: Joblib

Installation & Setup
1. Clone the Repository
Bash
git clone <your-repo-link>
cd fraud-detection-ai
2. Install Dependencies
Ensure you have the necessary libraries installed:

Bash
pip install fastapi uvicorn xgboost scikit-learn pandas numpy joblib requests
How to Run
Follow these steps in order to get the system up and running:

Step 1: Train the Model
Run the training script to generate synthetic data and create the model artifacts (fraud_model.pkl and scaler.pkl).

Bash
python train.py
Step 2: Start the API Server
Launch the FastAPI server. It will listen on http://127.0.0.1:8000.

Bash
python main.py
Step 3: Run the Test Client
In a new terminal window, run the interactive client to test the model.

Bash
python test_fraud.py
API Documentation
Once the server is running, you can access the interactive Swagger UI documentation at:
http://127.0.0.1:8000/docs

POST /predict
Request Body:

JSON
{
  "V1": -1.1,
  "V2": 2.5,
  "V3": -0.2,
  "V4": 0.5,
  "Amount": 150.0
}
Response:

JSON
{
  "status": "LEGITIMATE",
  "probability": "0.0124"
}
Model Details
The system uses an XGBoost Classifier. Because fraud is typically a "needle in a haystack" problem, the training script simulates an imbalanced dataset (99% legitimate, 1% fraudulent) to mimic real-world scenarios.

Note: The current train.py uses synthetic data. For production use, replace the data generation step with a real dataset (like the Kaggle Credit Card Fraud dataset).
