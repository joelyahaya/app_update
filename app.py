import streamlit as st
import pandas as pd
import pickle
import time

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(page_title="Diabetes Prediction - UMaT", page_icon="🩺", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            color: #006400;
            text-align: center;
            animation: fadeInDown 1.2s ease-in-out;
        }
        .sub-title {
            font-size: 20px;
            color: #FFD700;
            text-align: center;
            animation: fadeInUp 1.5s ease-in-out;
        }
        .prediction-box {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            animation: fadeIn 1.5s ease-in-out;
        }
        .credits {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-top: 30px;
            animation: fadeInUp 2s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">Diabetes Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">University of Mines and Technology</div>', unsafe_allow_html=True)

# Input form
with st.form("input_form"):
    st.subheader("Enter Patient Data:")
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose Level (Max: 1000)", min_value=1, max_value=1000)
    blood_pressure = st.number_input("Blood Pressure (Max: 140)", min_value=1, max_value=140)
    skin_thickness = st.number_input("Skin Thickness (Max: 99)", min_value=1, max_value=99)
    insulin = st.number_input("Insulin Level (Max: 1000)", min_value=1, max_value=1000)
    bmi = st.number_input("BMI (Max: 120)", min_value=1.0, max_value=120.0, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age", min_value=1, step=1)

    submit = st.form_submit_button("Predict Diabetes")

# Prediction logic
if submit:
    # Validate inputs
    invalid_fields = []
    if glucose <= 0 or glucose > 1000: invalid_fields.append("Glucose")
    if blood_pressure <= 0 or blood_pressure > 140: invalid_fields.append("Blood Pressure")
    if skin_thickness <= 0 or skin_thickness > 99: invalid_fields.append("Skin Thickness")
    if insulin <= 0 or insulin > 1000: invalid_fields.append("Insulin")
    if bmi <= 0 or bmi > 120: invalid_fields.append("BMI")
    if age <= 0: invalid_fields.append("Age")

    if invalid_fields:
        st.error(f"Invalid input detected in: {', '.join(invalid_fields)}. Please enter realistic values.")
    else:
        with st.spinner("Analyzing patient data..."):
            time.sleep(2)

        input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness,
                                    insulin, bmi, dpf, age]],
                                  columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                                           'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

        prediction = model.predict(input_data)[0]
        confidence = model.predict_proba(input_data)[0][prediction]

        if prediction == 1:
            st.markdown(f"""
                <div class='prediction-box' style='border-left: 6px solid red;'>
                    <h3 style='color:red;'>The patient is likely to have diabetes.</h3>
                    <p>Confidence: <strong>{confidence:.2%}</strong></p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='prediction-box' style='border-left: 6px solid green;'>
                    <h3 style='color:green;'>The patient is unlikely to have diabetes.</h3>
                    <p>Confidence: <strong>{confidence:.2%}</strong></p>
                </div>
            """, unsafe_allow_html=True)

# Credits
st.markdown("""
    <div class="credits">
        Designed and Developed By: <br>
        Yahaya Joel Casmed <br>
        Agyarko Samuel Boakye <br>
        Coffie Jones
    </div>
""", unsafe_allow_html=True)
