import requests
import json

url = 'http://localhost:5000/predict'

payload = {
    'Customer_Age': 30,
    'Gender': 'Male',
    'Policy_Type': 'Vehicle',
    'Claim_Amount': 60000,
    'Premium_Amount': 1000,
    'Claim_History_Count': 5,
    'Previous_Fraud_Flag': 1,
    'Days_To_Report': 45,
    'Claim_Type': 'Accident'
}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Response:", json.dumps(response.json(), indent=2))
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Failed to connect: {e}")
