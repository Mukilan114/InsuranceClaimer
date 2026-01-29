import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from predict_risk import predict_risk
import traceback

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for React

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Expected keys matching predict_risk requirement
        required_keys = [
            'Customer_Age', 'Gender', 'Policy_Type', 'Claim_Amount', 
            'Premium_Amount', 'Claim_History_Count', 'Previous_Fraud_Flag', 
            'Days_To_Report', 'Claim_Type'
        ]
        
        # Validate keys
        if not all(k in data for k in required_keys):
             return jsonify({'error': 'Missing required fields'}), 400
             
        # Convert numeric types if needed (JSON passing numbers is usually fine)
        
        risk, confidence = predict_risk(data)
        
        # Basic "ML Theory" explanation (rule-based for demo purposes)
        explanation = []
        if data['Previous_Fraud_Flag'] == 1:
            explanation.append("History of fraud significantly increases risk.")
        if data['Claim_Amount'] > 20000: # Arbitrary threshold for explanation
            explanation.append("High claim amounts are scrutinized more closely.")
        if data['Claim_History_Count'] > 2:
            explanation.append("Frequent past claims indicate higher probability of future claims.")
        
        if not explanation:
            explanation.append("Risk profile is balanced based on provided factors.")

        return jsonify({
            'risk_status': risk, 
            'confidence': confidence,
            'explanation': explanation
        })
        
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask API on port 5000...")
    app.run(debug=True, port=5000)
