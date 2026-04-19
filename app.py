import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="🏥")

st.title("🏥 Medical Insurance Cost Predictor")
st.write("Enter the details below to get an AI-powered insurance estimate.")

# 2. Load the Model
# This matches the 'insurance_model.pkl' file you just uploaded!
try:
    model = joblib.load('insurance_model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")

# 3. User Input Fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Are you a smoker?", options=["no", "yes"])

# 4. Prediction Logic
if st.button("Calculate Predicted Cost"):
    # Convert 'yes/no' to 1/0 for XGBoost
    smoker_val = 1 if smoker == "yes" else 0
    
    # Put inputs in an array (Matches: age, bmi, children, smoker)
    input_data = np.array([[age, bmi, children, smoker_val,0,0,0,0,0]])
    
    try:
        prediction = model.predict(input_data)
        
        # Show the result!
        st.success(f"### The predicted annual cost is: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Something went wrong with the prediction: {e}")
