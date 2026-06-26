import streamlit as st
import pandas as pd
import joblib

# 1. Load the saved model and columns
model = joblib.load('churn_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.set_page_config(page_title="Churn Predictor", page_icon="📞")

st.title("📞 Telecom Customer Churn Predictor")
st.markdown("Enter customer details below to see the probability of them leaving.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    tenure = st.slider("Tenure (How many months have they stayed?)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0, 150, 70)
    total_charges = st.number_input("Total Charges ($)", 0, 9000, 800)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col2:
    internet = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])
    security = st.selectbox("Online Security", ["Yes", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])
    billing = st.selectbox("Paperless Billing", ["Yes", "No"])

# 2. Process Input
if st.button("Predict Churn Status"):
    # Create an empty row with all columns set to 0
    input_data = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Fill in numerical data
    input_data['tenure'] = tenure
    input_data['MonthlyCharges'] = monthly_charges
    input_data['TotalCharges'] = total_charges
    
    # Logic for Contract
    if contract == "One year": input_data['Contract_One year'] = 1
    if contract == "Two year": input_data['Contract_Two year'] = 1
    
    # Logic for Internet
    if internet == "Fiber optic": input_data['InternetService_Fiber optic'] = 1
    if internet == "No": input_data['InternetService_No'] = 1
    
    # Logic for Security
    if security == "Yes": input_data['OnlineSecurity_Yes'] = 1
    
    # Logic for Tech Support
    if tech_support == "Yes": input_data['TechSupport_Yes'] = 1
    
    # Logic for Billing
    if billing == "Yes": input_data['PaperlessBilling_Yes'] = 1

    # 3. Make Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # 4. Show Results
    st.divider()
    if prediction == 1:
        st.error(f"### ⚠️ Result: HIGH RISK")
        st.write(f"The model is **{probability:.1%}** confident this customer will leave.")
    else:
        st.success(f"### ✅ Result: LOW RISK")
        st.write(f"The model is **{1 - probability:.1%}** confident this customer will stay.")
        
    st.progress(probability)