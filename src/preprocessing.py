import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib

def load_data(filepath):
    """Loads the dataset from csv."""
    return pd.read_csv(filepath)

def preprocess_data(df, target_column='Risk_Label', save_scalers=False):
    """
    Preprocesses the data: encodes categoricals, scales features, splits data.
    """
    # Handle Categoricals
    encoders = {}
    categorical_cols = ['Gender', 'Policy_Type', 'Claim_Type', 'Risk_Label']
    
    # We need to handle inference time encoding carefully, but for this project we'll fit on the whole dataset or training set
    # For simplicity in this project scope, we will use LabelEncoder. 
    # Note: For production systems, OneHotEncoder is often safer for nominal data, but we follow the notebook style.
    
    df_processed = df.copy()
    
    for col in categorical_cols:
        if col in df_processed.columns:
            le = LabelEncoder()
            df_processed[col] = le.fit_transform(df_processed[col])
            encoders[col] = le
            
    # Drop IDs
    if 'Claim_ID' in df_processed.columns:
        df_processed = df_processed.drop('Claim_ID', axis=1)
        
    X = df_processed.drop(target_column, axis=1)
    y = df_processed[target_column]
    
    # Scale Features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # feature names
    feature_names = X.columns.tolist()
    
    if save_scalers:
        joblib.dump(scaler, 'outputs/scaler.pkl')
        joblib.dump(encoders, 'outputs/encoders.pkl')
        
    return X_scaled, y, feature_names, scaler, encoders

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)
