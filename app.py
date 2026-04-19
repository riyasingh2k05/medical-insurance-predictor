import streamlit as st
import pandas as pd
import joblib

# 1. Load your model (make sure the filename matches what's in your repo)
# model = joblib.load('medical_insurance_model.pkl')

st.title("Medical Insurance Cost Predictor")
st.write("Enter your details below to estimate your insurance costs.")

# 2. Create Input Fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
smoker = st.selectbox("Are you a smoker?", ["yes", "no"])

# 3. Prediction Logic
if st.button("Predict Cost"):
    # Here is where you would call your model.predict()
    # For now, let's just show a test message to see if it works:
    st.success(f"Form submitted for Age: {age}")
