import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocessing import load_data, preprocess_data, split_data

def train():
    # Load and Preprocess
    print("Loading data...")
    df = load_data('data/insurance_claims.csv')
    X_scaled, y, feature_names, scaler, encoders = preprocess_data(df, save_scalers=True)
    
    X_train, X_test, y_train, y_test = split_data(X_scaled, y)
    
    # Train Models
    models = {
        'Logistic Regression': LogisticRegression(),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(n_estimators=100)
    }
    
    best_model = None
    best_acc = 0
    best_model_name = ""
    
    results = {}
    
    print("Training models...")
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results[name] = acc
        print(f"{name} Accuracy: {acc:.4f}")
        
        if acc > best_acc:
            best_acc = acc
            best_model = model
            best_model_name = name
            
    print(f"\nBest Model: {best_model_name} with Accuracy: {best_acc:.4f}")
    
    # Save Best Model
    joblib.dump(best_model, 'outputs/model.pkl')
    print("Model saved to outputs/model.pkl")

if __name__ == "__main__":
    train()
