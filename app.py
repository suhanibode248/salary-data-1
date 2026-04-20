import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model_result.pkl")

# Debug (remove later)
st.write("Model type:", type(model))

# UI
experience = st.slider("Years of Experience", 0, 20, 5)

if st.button("Predict Salary"):
    try:
        # Convert to proper format
        exp_input = np.array([[float(experience)]])
        
        prediction = model.predict(exp_input)
        
        st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")
    
    except Exception as e:
        st.error(f"Error: {e}")
