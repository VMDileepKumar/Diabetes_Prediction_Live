"""Streamlit interface for the trained diabetes prediction model."""

import streamlit as st

from src.predict import predict_diabetes

st.set_page_config(page_title="Diabetes Prediction", page_icon="D", layout="centered")
st.title("Diabetes Prediction")
st.write("Enter the measurements below to view the model's predicted class.")

with st.form("prediction_form"):
    left_column, right_column = st.columns(2)
    with left_column:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
        glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)
        blood_pressure = st.number_input(
            "Blood pressure", min_value=0, max_value=200, value=70
        )
        skin_thickness = st.number_input(
            "Skin thickness", min_value=0, max_value=100, value=20
        )
    with right_column:
        insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
        bmi = st.number_input("BMI", min_value=0.0, max_value=80.0, value=25.0)
        pedigree = st.number_input(
            "Diabetes pedigree function",
            min_value=0.0,
            max_value=3.0,
            value=0.5,
            step=0.01,
        )
        age = st.number_input("Age", min_value=1, max_value=120, value=33)

    submitted = st.form_submit_button("Predict")

if submitted:
    input_values = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": pedigree,
        "Age": age,
    }
    try:
        outcome = predict_diabetes(input_values)
    except FileNotFoundError as error:
        st.error(str(error))
    else:
        if outcome == 1:
            st.warning("The model predicts diabetes (class 1).")
        else:
            st.success("The model predicts no diabetes (class 0).")

st.caption("This model is for educational use and is not a medical diagnosis.")