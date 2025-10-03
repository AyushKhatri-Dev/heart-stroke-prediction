import streamlit as st
import pandas as pd
import joblib

# Load models and expected columns
model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# Title and instructions
st.title("Heart Stroke Prediction ❤️")
st.markdown("Provide the following details:")

# Input fields
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ['M', 'F'])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])    
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0, step=0.1)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Prediction button
if st.button("Predict"):

    # Raw inputs with base features
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak
    }

    # One-hot encoded categorical values
    categorical_features = {
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Merge into one dictionary
    full_input = {**raw_input, **categorical_features}

    # Create input DataFrame
    input_df = pd.DataFrame([full_input])

    # Add any missing expected columns as 0
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match training
    input_df = input_df[expected_columns]

    # Scale and predict
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
