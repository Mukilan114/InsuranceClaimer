import streamlit as st
import pandas as pd
import sys
import os

# Add src to path so we can import predict_risk
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from predict_risk import predict_risk

st.set_page_config(page_title="Insurance Claim Risk Predictor", page_icon="🛡️", layout="centered")

st.title("🛡️ Insurance Claim Risk Classifier")
st.markdown("Enter the claim details below to predict the risk level.")

with st.form("claim_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Customer Age", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        policy_type = st.selectbox("Policy Type", ["Health", "Vehicle", "Property", "Life"])
        claim_type = st.selectbox("Claim Type", ["Accident", "Theft", "Natural Disaster", "Medical"])
        
    with col2:
        claim_amount = st.number_input("Claim Amount ($)", min_value=0.0, value=5000.0)
        premium_amount = st.number_input("Premium Amount ($)", min_value=0.0, value=500.0)
        claim_history = st.number_input("Previous Claims", min_value=0, max_value=20, value=0)
        days_report = st.number_input("Days to Report", min_value=0, value=0)
        
    fraud_history = st.checkbox("Has Previous Fraud History?")
    
    submitted = st.form_submit_button("Predict Risk")

if submitted:
    # Prepare input
    # Note: fraud_history is boolean, our model expects 0 or 1
    input_data = {
        'Customer_Age': age,
        'Gender': gender,
        'Policy_Type': policy_type,
        'Claim_Amount': claim_amount,
        'Premium_Amount': premium_amount,
        'Claim_History_Count': claim_history,
        'Previous_Fraud_Flag': 1 if fraud_history else 0,
        'Days_To_Report': days_report,
        'Claim_Type': claim_type
    }
    
    try:
        risk = predict_risk(input_data)
        
        st.divider()
        st.subheader("Prediction Result")
        
        if risk == 'High Risk':
            st.error(f"⚠️ **{risk}**")
            st.warning("This claim shows characteristics associated with high risk. Manual review is recommended.")
        else:
            st.success(f"✅ **{risk}**")
            st.info("This claim appears to be low risk.")
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
