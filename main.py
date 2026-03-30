from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Load assets
model = joblib.load('fraud_model.pkl')
scaler = joblib.load('scaler.pkl')

app = FastAPI()

class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    Amount: float

@app.post("/predict")
def predict(data: Transaction):
    # Prepare data for model
    input_df = pd.DataFrame([data.dict()])
    input_df['Amount'] = scaler.transform(input_df[['Amount']])
    
    # Predict
    prob = model.predict_proba(input_df)[0][1]
    is_fraud = "FRAUD DETECTED" if prob > 0.5 else "LEGITIMATE"
    
    return {"status": is_fraud, "probability": f"{prob:.4f}"}

if __name__ == "__main__":
    import uvicorn
    print("\nStarting the API Server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)