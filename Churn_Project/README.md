# 📞 Telecom Customer Churn Predictor

### 🚀 Project Overview
This is a Machine Learning application that predicts the probability of a customer leaving a telecom service. By analyzing customer behavior—such as contract type, tenure, and monthly charges—the AI model identifies "at-risk" customers so the company can take action to retain them.

### 📊 Features
- **Real-time Prediction:** Enter customer data and get an instant Churn vs. Stay result.
- **Probability Scoring:** The app shows exactly how confident the AI is in its prediction (e.g., 85% likely to churn).
- **Key Indicators:** Factors in critical data like Internet Service Type, Online Security, and Contract length.

### 🛠️ Tech Stack
- **Python** (Programming Language)
- **Pandas** (Data Manipulation)
- **Scikit-Learn** (Machine Learning Modeling)
- **Random Forest** (The AI Algorithm)
- **Streamlit** (Web Dashboard Framework)

### 📁 Project Structure
- `app.py`: The main code for the web application.
- `churn_model.pkl`: The trained "brain" of the AI.
- `model_columns.pkl`: The list of data features used by the model.
- `README.md`: Project documentation.

### ⚙️ How to Run
1. Open your terminal or command prompt.
2. Install the required libraries:
   ```bash
   pip install streamlit pandas joblib scikit-learn

### Run the application:
    streamlit run app.py

### 📊 Model Performance
    Accuracy: ~80%
    Best Features: Tenure, Contract Type, and Internet Service type were found to be the most important factors in predicting churn.