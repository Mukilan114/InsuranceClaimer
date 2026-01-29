# Insurance Claim Risk Classification - Project Report

## 1. Introduction
The insurance industry faces significant challenges in managing claims efficiently. Fraudulent or high-risk claims can lead to substantial financial losses. This project aims to mitigate these risks by developing a Machine Learning-based classification system.

## 2. Problem Statement
Manual processing of insurance claims is time-consuming and prone to errors. Identifying high-risk claims requires analyzing multiple factors such as claim amount, history, and policy details. The goal is to automate this risk assessment process.

## 3. Objectives
- develop a machine learning model to classify claims as "High Risk" or "Low Risk".
- Identify key features contributing to claim risk.
- Provide a user-friendly interface for risk prediction.

## 4. Dataset Description
A synthetic dataset was generated to simulate realistic scenarios.
- **Size**: >1000 records
- **Features**: 
    - Customer Demographics (Age, Gender)
    - Policy Details (Type, Premium)
    - Claim Details (Amount, Type, History, Fraud Flag, Days to Report)
- **Target**: Risk_Label (High Risk, Low Risk)

## 5. Data Preprocessing
- **Handling Missing Values**: The synthetic generation ensured clean data, but the pipeline includes checks.
- **Encoding**: Label Encoding was used for categorical variables (Gender, Policy_Type, Claim_Type).
- **Scaling**: Standard Scaler was applied to normalize numerical features.
- **Splitting**: Data split into 80% training and 20% testing sets.

## 6. Exploratory Data Analysis (EDA)
Key insights observed:
- High claim amounts generally correlate with higher risk.
- A history of previous fraud is a strong indicator of high risk.
- Late reporting (high `Days_To_Report`) often flags a claim as risky.

## 7. Model Building
Three models were trained and compared:
1. **Logistic Regression**: A baseline linear model.
2. **Decision Tree**: Captures non-linear relationships.
3. **Random Forest**: An ensemble method for robust predictions.

## 8. Model Evaluation
The models were evaluated based on Accuracy, Precision, Recall, and F1-Score.
*Note: Run `src/evaluate_model.py` to generate the latest metrics.*

**Selected Model**: Random Forest was chosen for its superior ability to handle complex feature interactions and prevent overfitting compared to a single Decision Tree.

## 9. Feature Importance
Analysis revealed that:
- `Previous_Fraud_Flag`
- `Claim_Amount`
- `Claim_History_Count`
are the most significant predictors of risk.

## 10. Conclusion
The developed system effectively classifies insurance claim risks. The Random Forest model demonstrates high accuracy, making it a viable tool for automated risk assessment.

## 11. Future Scope
- Incorporate real-world datasets for better generalization.
- Deploy the model as a cloud-based API.
- Implement deep learning techniques for larger datasets.
