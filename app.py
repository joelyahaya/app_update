
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import time

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Set page config
st.set_page_config(page_title="Diabetes Prediction - UMaT", page_icon="🩺", layout="centered")

# Custom CSS for animations and theme
st.markdown("""
    <style>
        body {
            background-color: #F5F5F5;
        }
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
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .prediction-box {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            animation: fadeIn 1.5s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
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

# Form for user input
with st.form("input_form"):
    st.subheader("Enter Patient Data:")
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin Level", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age", min_value=0, step=1)

    submit = st.form_submit_button("Predict Diabetes")

if submit:
    # Loading animation
    with st.spinner("Analyzing patient data..."):
        time.sleep(2)

    data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness,
                          insulin, bmi, dpf, age]],
                        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

    prediction = model.predict(data)[0]

    # Result
    if prediction == 1:
        st.markdown(f"<div class='prediction-box' style='border-left: 6px solid red;'><h3 style='color:red;'>The patient is likely to have diabetes.</h3></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='prediction-box' style='border-left: 6px solid green;'><h3 style='color:green;'>The patient is unlikely to have diabetes.</h3></div>", unsafe_allow_html=True)

# Credits
st.markdown("""
    <div class="credits">
        Designed and Developed By: <br>
        Yahaya Joel Casmed <br>
        Agyarko Samuel Boakye <br>
        Coffie Jones
    </div>
""", unsafe_allow_html=True)
