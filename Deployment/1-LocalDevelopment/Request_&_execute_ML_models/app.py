# BUCKET_NAME="full-stack-assets"
# KEY="Deployment/house_prices_model.joblib"
# OBJECT_URL="https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/house_prices_model.joblib"

from joblib import load
import requests 
import pandas as pd
from io import BytesIO

## Load Data 
r = requests.get("https://charlestng-house-prices-simple-api.hf.space/data")
test_data = pd.read_json(r.json(), orient="split")
## Splitting into X and y
X = test_data.iloc[:, :-1]
y = test_data.iloc[:, -1]

## Load model 
print("Loading model...")
r = requests.get('https://full-stack-assets.s3.eu-west-3.amazonaws.com/Deployment/house_prices_model.joblib')
mfile = BytesIO(r.content)
model = load(mfile)
print("model loaded!\n")


print("Using model to make prediction...")
prediction = model.predict(X)[0]
print(f"According to our model, this house should cost: {prediction}\n")

print("Checking accuracy...")
truth = y.iloc[0]
print(f"House actual price is: {truth}")
print(f"Our model is {abs(prediction - truth)} away from the truth!")

