import pandas as pd
import numpy as np
import random

def generate_data(num_records=1000):
    np.random.seed(42)
    random.seed(42)

    data = []
    
    for i in range(num_records):
        claim_id = f"CLM{10000+i}"
        customer_age = np.random.randint(18, 90)
        gender = np.random.choice(['Male', 'Female'])
        policy_type = np.random.choice(['Health', 'Vehicle', 'Property', 'Life'])
        
        # Base claim amount varies by policy type
        if policy_type == 'Health':
            base_claim = np.random.uniform(1000, 50000)
        elif policy_type == 'Vehicle':
            base_claim = np.random.uniform(1000, 30000)
        elif policy_type == 'Property':
            base_claim = np.random.uniform(5000, 100000)
        else: # Life
            base_claim = np.random.uniform(50000, 500000)
            
        claim_amount = round(base_claim, 2)
        premium_amount = round(base_claim * np.random.uniform(0.01, 0.1) + np.random.uniform(100, 500), 2)
        
        claim_history_count = np.random.choice([0, 1, 2, 3, 4, 5], p=[0.4, 0.25, 0.15, 0.1, 0.05, 0.05])
        previous_fraud_flag = 1 if (np.random.random() < 0.05 or (claim_history_count > 3 and np.random.random() < 0.3)) else 0
        
        days_to_report = np.random.randint(0, 60)
        if np.random.random() < 0.1: # Occasionally very late reporting
            days_to_report += np.random.randint(30, 300)
            
        claim_type = np.random.choice(['Accident', 'Theft', 'Natural Disaster', 'Medical'])
        
        # Risk Logic
        risk_score = 0
        if claim_amount > 50000: risk_score += 2
        if claim_history_count > 2: risk_score += 2
        if previous_fraud_flag == 1: risk_score += 4
        if days_to_report > 30: risk_score += 1
        if customer_age < 25 or customer_age > 75: risk_score += 1
        
        # Random noise
        risk_score += np.random.normal(0, 1)

        risk_label = 'High Risk' if risk_score > 3.5 else 'Low Risk'

        data.append([
            claim_id, customer_age, gender, policy_type, claim_amount, 
            premium_amount, claim_history_count, previous_fraud_flag, 
            days_to_report, claim_type, risk_label
        ])

    columns = [
        'Claim_ID', 'Customer_Age', 'Gender', 'Policy_Type', 'Claim_Amount',
        'Premium_Amount', 'Claim_History_Count', 'Previous_Fraud_Flag',
        'Days_To_Report', 'Claim_Type', 'Risk_Label'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    return df

if __name__ == "__main__":
    df = generate_data(1200) # Generating slightly more than 1000
    df.to_csv('data/insurance_claims.csv', index=False)
    print("Data generated at data/insurance_claims.csv")
    print(df.head())
    print(df['Risk_Label'].value_counts())
