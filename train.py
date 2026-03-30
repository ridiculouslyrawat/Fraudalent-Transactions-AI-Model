import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
import joblib

print("--- Step 1: Generating Synthetic Data ---")
# Creating 1000 fake transactions (990 legit, 10 fraud)
data = np.random.randn(1000, 5) # 5 features: V1, V2, V3, V4, Amount
labels = np.array([0]*990 + [1]*10)
df = pd.DataFrame(data, columns=['V1', 'V2', 'V3', 'V4', 'Amount'])

print("--- Step 2: Scaling Data ---")
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])

print("--- Step 3: Training XGBoost Model ---")
model = XGBClassifier()
model.fit(df, labels)

print("--- Step 4: Saving Model Assets ---")
joblib.dump(model, 'fraud_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Done! Files 'fraud_model.pkl' and 'scaler.pkl' created.\n")