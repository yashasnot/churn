import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📉 Customer Churn Prediction System")
st.caption("Logistic Regression • ROC-AUC ≈ 0.84 • Threshold = 0.35")
st.write("Predict whether a customer is likely to churn.")

# Input fields
tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

# Build input dataframe
input_df = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges],
    "Contract": [contract],
    "InternetService": [internet],
    "PaymentMethod": [payment]
})
if st.button("Predict Churn"):
    prob = model.predict_proba(input_df)[0][1]

    st.metric("Churn Probability", f"{prob:.2%}")

    if prob >= 0.35:
        st.error("⚠️ High Churn Risk")
    else:
        st.success("✅ Low Churn Risk")
        
st.markdown("---")
st.caption("Built by Yashas Raina • ML Project")