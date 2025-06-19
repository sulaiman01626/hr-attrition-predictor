
import streamlit as st
import joblib
import numpy as np

model = joblib.load("attrition_model.pkl")
features = joblib.load("features.pkl")

st.title("🧑‍💼 Employee Attrition Predictor")

inputs = []
for feature in features:
    val = st.number_input(f"{feature}", value=0)
    inputs.append(val)

if st.button("Predict"):
    pred = model.predict([inputs])
    result = "⚠️ Will Leave" if pred[0] == 1 else "✅ Will Stay"
    st.success(f"Prediction: {result}")
