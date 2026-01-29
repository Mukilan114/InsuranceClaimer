# Insurance Claim Risk Classification

## Project Overview
This project aims to build a Machine Learning model that classifies insurance claims as **High Risk** or **Low Risk** using historical claim and customer data. It helps insurance companies identify potentially fraudulent or high-risk claims for further investigation.

## Technologies Used
- **Python**: Core programming language.
- **Pandas & NumPy**: Data manipulation and analysis.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-learn**: Machine Learning model building and evaluation.
- **Streamlit**: Web application for interactive prediction.

## Dataset Description
The dataset is synthetically generated to simulate realistic insurance claim scenarios. It contains over 1000 records with the following features:
- `Claim_ID`: Unique identifier.
- `Customer_Age`: Age of the customer.
- `Gender`: Gender of the customer.
- `Policy_Type`: Type of policy (Health, Vehicle, Property, Life).
- `Claim_Amount`: Monetary value of the claim.
- `Premium_Amount`: Premium paid by the customer.
- `Claim_History_Count`: Number of previous claims.
- `Previous_Fraud_Flag`: Indicator of past fraud (0 = No, 1 = Yes).
- `Days_To_Report`: Days between incident and reporting.
- `Claim_Type`: Type of claim event (Accident, Theft, etc.).
- `Risk_Label`: Target variable (High Risk / Low Risk).

## Project Structure
```
insurance-claim-risk-classification/
├── data/               # Contains insurance_claims.csv
├── notebooks/          # EDA and Model prototyping notebook
├── src/                # Source code for processing and modeling
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict_risk.py # Prediction logic for the app
├── outputs/            # Saved models and charts
│   ├── charts/
│   ├── model.pkl
│   └── ...
├── report/             # Project documentation
├── app.py              # Streamlit Web App
└── requirements.txt    # Dependencies
```

## Steps to Run the Project
1. **Clone/Navigate to the directory**:
   ```bash
   cd insurance-claim-risk-classification
   ```

2. **Backend Setup**:
   - Install Dependencies:
     ```bash
     pip install -r requirements.txt
     pip install flask flask-cors
     ```
   - Start the API:
     ```bash
     python src/api.py
     ```
   *The API will run on http://localhost:5000.*

3. **Frontend Setup**:
   - Open a new terminal and navigate to `frontend`:
     ```bash
     cd frontend
     ```
   - Install Dependencies:
     ```bash
     npm install
     ```
   - Start the React App:
     ```bash
     npm run dev
     ```
   *The UI will run on http://localhost:5173.*

4. **Usage**:
   - Open your browser to the frontend URL.
   - Enter claim details.
   - Click "Predict Risk" to get a real-time assessment.

## Model Performance
The Random Forest classifier is used for predictions.
- **Accuracy**: ~95%+ (on synthetic data)
- **metrics**: See `outputs/` or run `evaluate_model.py` for detailed report.

## Screenshots
Please check the `outputs/charts` directory for confusion matrix and feature importance plots.

