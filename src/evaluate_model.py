import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from preprocessing import load_data, preprocess_data, split_data

def evaluate():
    # Load Data and Model
    df = load_data('data/insurance_claims.csv')
    X_scaled, y, feature_names, _, _ = preprocess_data(df)
    _, X_test, _, y_test = split_data(X_scaled, y)
    
    model = joblib.load('outputs/model.pkl')
    
    y_pred = model.predict(X_test)
    
    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print("--- Model Evaluation ---")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig('outputs/charts/confusion_matrix.png')
    print("Confusion matrix saved to outputs/charts/confusion_matrix.png")
    
    # Feature Importance (if applicable)
    if hasattr(model, 'feature_importances_'):
        plt.figure(figsize=(10, 6))
        feature_importances = pd.Series(model.feature_importances_, index=feature_names)
        feature_importances.nlargest(10).plot(kind='barh')
        plt.title('Feature Importance')
        plt.savefig('outputs/charts/feature_importance.png')
        print("Feature importance saved to outputs/charts/feature_importance.png")

if __name__ == "__main__":
    evaluate()
