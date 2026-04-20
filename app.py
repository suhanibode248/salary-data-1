import streamlit as st
import pickle
import numpy as np

with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("💼 Salary Prediction App")
st.write("Years of Experience daalo aur salary predict karo")

experience = st.slider("Years of Experience", 0, 20, 5)

if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Predicted Salary: $ {prediction[0]:,.2f}")
