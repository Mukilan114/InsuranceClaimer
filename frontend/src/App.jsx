import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    Customer_Age: 30,
    Gender: 'Male',
    Policy_Type: 'Vehicle',
    Claim_Amount: 5000,
    Premium_Amount: 500,
    Claim_History_Count: 0,
    Previous_Fraud_Flag: false,
    Days_To_Report: 0,
    Claim_Type: 'Accident'
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    // Frontend Constraints Validation
    if (formData.Customer_Age < 18 || formData.Customer_Age > 100) {
      setError("Customer Age must be between 18 and 100.");
      return;
    }
    if (formData.Claim_Amount < 0) {
      setError("Claim Amount cannot be negative.");
      return;
    }
    if (formData.Premium_Amount < 0) {
      setError("Premium Amount cannot be negative.");
      return;
    }

    try {
      const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
      const response = await fetch(`${API_URL}/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ...formData,
          Previous_Fraud_Flag: formData.Previous_Fraud_Flag ? 1 : 0,
          Customer_Age: parseInt(formData.Customer_Age),
          Claim_Amount: parseFloat(formData.Claim_Amount),
          Premium_Amount: parseFloat(formData.Premium_Amount),
          Claim_History_Count: parseInt(formData.Claim_History_Count),
          Days_To_Report: parseInt(formData.Days_To_Report)
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Failed to fetch prediction. Ensure the backend is running.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Format currency helper
  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount);
  };

  return (
    <div className="container">
      <header>
        <h1>🛡️ Insurance Claim Risk Classifier</h1>
        <p className="subtitle">Advanced Machine Learning Risk Assessment System</p>
      </header>

      <div className="main-content">
        <div className="form-card">
          <h2>📝 Claim Details</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-grid">
              <div className="form-group">
                <label>Customer Age</label>
                <input type="number" name="Customer_Age" value={formData.Customer_Age} onChange={handleChange} min="18" max="100" required />
              </div>

              <div className="form-group">
                <label>Gender</label>
                <select name="Gender" value={formData.Gender} onChange={handleChange}>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>

              <div className="form-group">
                <label>Policy Type</label>
                <select name="Policy_Type" value={formData.Policy_Type} onChange={handleChange}>
                  <option value="Health">Health</option>
                  <option value="Vehicle">Vehicle</option>
                  <option value="Property">Property</option>
                  <option value="Life">Life</option>
                </select>
              </div>

              <div className="form-group">
                <label>Claim Type</label>
                <select name="Claim_Type" value={formData.Claim_Type} onChange={handleChange}>
                  <option value="Accident">Accident</option>
                  <option value="Theft">Theft</option>
                  <option value="Natural Disaster">Natural Disaster</option>
                  <option value="Medical">Medical</option>
                </select>
              </div>

              <div className="form-group">
                <label>Claim Amount (USD)</label>
                <div className="input-icon-wrapper">
                  <span className="currency-symbol">$</span>
                  <input type="number" name="Claim_Amount" value={formData.Claim_Amount} onChange={handleChange} min="0" step="0.01" required />
                </div>
              </div>

              <div className="form-group">
                <label>Premium Amount (USD)</label>
                <div className="input-icon-wrapper">
                  <span className="currency-symbol">$</span>
                  <input type="number" name="Premium_Amount" value={formData.Premium_Amount} onChange={handleChange} min="0" step="0.01" required />
                </div>
              </div>

              <div className="form-group">
                <label>Previous Claims</label>
                <input type="number" name="Claim_History_Count" value={formData.Claim_History_Count} onChange={handleChange} min="0" max="20" required />
              </div>

              <div className="form-group">
                <label>Days To Report</label>
                <input type="number" name="Days_To_Report" value={formData.Days_To_Report} onChange={handleChange} min="0" required />
              </div>

              <div className="form-group full-width checkbox-group">
                <label>
                  <input type="checkbox" name="Previous_Fraud_Flag" checked={formData.Previous_Fraud_Flag} onChange={handleChange} />
                  Has Previous Fraud History?
                </label>
              </div>
            </div>

            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? 'Analyzing...' : 'Predict Risk'}
            </button>
          </form>
        </div>

        <div className="right-panel">
          <div className="result-card">
            {result ? (
              <div className={`result-box ${result.risk_status === 'High Risk' ? 'high-risk' : 'low-risk'}`}>
                <h3>Prediction Result</h3>
                <div className="risk-badge">{result.risk_status}</div>

                <div className="confidence-section">
                  <span>Model Confidence:</span>
                  <div className="progress-bar">
                    <div className="progress-fill" style={{ width: `${(result.confidence * 100).toFixed(1)}%` }}></div>
                  </div>
                  <span className="confidence-value">{(result.confidence * 100).toFixed(1)}%</span>
                </div>

                <div className="explanation">
                  <h4>🔍 AI Analysis:</h4>
                  <ul>
                    {result.explanation.map((item, index) => (
                      <li key={index}>{item}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ) : (
              <div className="placeholder-box">
                <h3>Analysis Pending</h3>
                <p>Enter claim details and click predict to see the risk assessment.</p>
                {error && <p className="error-msg">{error}</p>}
              </div>
            )}
          </div>

          <div className="info-card">
            <h3>🎓 About the Model</h3>
            <p>
              This system uses a <strong>Random Forest Classifier</strong>, an ensemble machine learning algorithm.
              It aggregates predictions from multiple decision trees to improve accuracy and control over-fitting.
            </p>
            <p>
              <strong>Key Features Analyzed:</strong>
              <ul>
                <li>Claim Amount & History</li>
                <li>Policy details</li>
                <li>Fraud indicators</li>
              </ul>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
