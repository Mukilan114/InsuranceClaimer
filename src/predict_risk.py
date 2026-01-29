import pandas as pd
import joblib
import numpy as np

def predict_risk(claim_details):
    """
    Predicts risk for a given dictionary of claim details.
    """
    # Load artifacts
    model = joblib.load('outputs/model.pkl')
    scaler = joblib.load('outputs/scaler.pkl')
    encoders = joblib.load('outputs/encoders.pkl')
    
    # Create DataFrame from input
    input_df = pd.DataFrame([claim_details])
    
    # Preprocess Input (Similar to training)
    # Encode
    for col, le in encoders.items():
        if col in input_df.columns and col != 'Risk_Label':
            # Handle unseen labels carefully, or assuming valid input for now
            try:
                input_df[col] = le.transform(input_df[col])
            except ValueError:
                # If unseen label, assign a default or raise error. 
                # For this demo, we might just assume valid input or map to 0
                input_df[col] = 0 
                
    # Ensure correct column order (excluding Risk_Label and Claim_ID)
    # We need the feature names used during training.
    # We can infer them from the scaler (if we saved feature order) or hardcode.
    # In preprocessing.py we returned feature_names, but didn't save them explicitly aside from code logic.
    # Let's align with the order:
    cols_order = [
         'Customer_Age', 'Gender', 'Policy_Type', 'Claim_Amount',
         'Premium_Amount', 'Claim_History_Count', 'Previous_Fraud_Flag',
         'Days_To_Report', 'Claim_Type'
    ]
    
    input_df = input_df[cols_order]
    
    # Scale
    input_scaled = scaler.transform(input_df)
    
    # Predict
    prob = model.predict_proba(input_scaled)[0]
    prediction = model.predict(input_scaled)[0]
    
    # Get probability of the predicted class
    # Classes are likely ['High Risk', 'Low Risk'] or similar. 
    # specific prob depends on class order. model.classes_ 
    
    # Let's return the probability of "High Risk" specifically if possible, or just the max prob.
    # We need to know which class index corresponds to "High Risk".
    # Since we used LabelEncoder, we can find it.
    
    risk_label = encoders['Risk_Label'].inverse_transform([prediction])[0]
    
    # confidence score (max probability)
    confidence = float(np.max(prob))
    
    return risk_label, confidence

if __name__ == "__main__":
    # Test Prediction
    sample = {
        'Customer_Age': 45,
        'Gender': 'Male',
        'Policy_Type': 'Vehicle',
        'Claim_Amount': 15000,
        'Premium_Amount': 1200,
        'Claim_History_Count': 1,
        'Previous_Fraud_Flag': 0,
        'Days_To_Report': 5,
        'Claim_Type': 'Accident'
    }
    print(f"Prediction for sample: {predict_risk(sample)}")
