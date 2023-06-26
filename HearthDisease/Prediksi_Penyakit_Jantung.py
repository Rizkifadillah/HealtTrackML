# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:40:40 2023

@author: rizki
"""


import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler


# Load model
model = pickle.load(open('D:/Data Science/Course Langing/Part 16 - Siddhardhan tutorial/Deploy Project/jantung_model.pkl', 'rb'))

# Load scaler
scaler = pickle.load(open('D:/Data Science/Course Langing/Part 16 - Siddhardhan tutorial/Deploy Project/scaler.pkl', 'rb'))


#load_model_diabetes = load_model('D:/Data Science/Course Langing/Part 16 - Siddhardhan tutorial/Deploy Project/diabetes_model.sav')

def preprocess_input(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    # input_scaled = scaler.transform(input_array)
    # return input_scaled
    return input_array


# Main function for Streamlit app
def main():
    # Set page title
    st.title("Prediksi Penyakit Jantung")

    # Create input fields for user
    age = st.slider("Usia", 0, 100, 50)
    sex = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
    chest_pain_type = st.selectbox("Tipe Nyeri Dada",
                                   ["Typical angina", "Non-anginal pain", "Atypical angina", "Asymptomatic"])
    resting_blood_pressure = st.slider("Tekanan Darah Istirahat", 90, 200, 120)
    cholestoral = st.slider("Kolesterol", 100, 600, 250)
    fasting_blood_sugar = st.selectbox("Gula Darah Puasa",
                                       ["Kurang dari 120 mg/dl", "Lebih dari 120 mg/dl"])
    rest_ecg = st.selectbox("Elektrokardiografi Istirahat",
                            ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
    Max_heart_rate = st.slider("Detak Jantung Maksimum", 50, 220, 150)
    exercise_induced_angina = st.selectbox("Angina yang Diprovokasi oleh Olahraga",
                                           ["Tidak", "Ya"])
    oldpeak = st.slider("Depresi ST yang Diinduksi oleh Olahraga", 0.0, 7.0, 3.0)
    slope = st.selectbox("Slope", ["Upsloping" , "Flat", "Downsloping"])
    vessels_colored_by_flourosopy = st.selectbox("Jumlah Saluran yang Diberi Warna",
                                                 ["0", "1", "2", "3", "4"])
    thalassemia = st.selectbox("Hasil Tes Thalassemia",
                               ["No", "Normal", "Reversable Defect","Fixed Defect"])

    # Create a button for prediction
    if st.button("Prediksi"):
        # Preprocess input data
        
        # Preprocess input data
        if chest_pain_type == "Typical angina":
            chest_pain_type = 0
        elif chest_pain_type == "Non-anginal pain":
            chest_pain_type = 1
        elif chest_pain_type == "Atypical angina":
            chest_pain_type = 2
        elif chest_pain_type == "Asymptomatic":
            chest_pain_type = 3
        else:
            # Handle the case when an invalid value is selected
            st.write("Pilihan chest_pain_type tidak valid.")

        # Preprocess input data
        if rest_ecg == "Normal":
            rest_ecg = 0
        elif rest_ecg == "ST-T wave abnormality":
            rest_ecg = 1
        elif rest_ecg == "Left ventricular hypertrophy":
            rest_ecg = 2
        else:
            # Handle the case when an invalid value is selected
            st.write("Pilihan rest_ecg tidak valid.")
        
        # Preprocess input data
        if vessels_colored_by_flourosopy == "0":
            vessels_colored_by_flourosopy = 0
        elif vessels_colored_by_flourosopy == "1":
            vessels_colored_by_flourosopy = 1
        elif vessels_colored_by_flourosopy == "2":
            vessels_colored_by_flourosopy = 2
        elif vessels_colored_by_flourosopy == "3":
            vessels_colored_by_flourosopy = 3
        elif vessels_colored_by_flourosopy == "4":
            vessels_colored_by_flourosopy = 4
        else:
            # Handle the case when an invalid value is selected
            st.write("Pilihan vessels_colored_by_flourosopy tidak valid.")

        # Preprocess input data
        if thalassemia == "No":
            thalassemia = 0
        elif thalassemia == "Normal":
            thalassemia = 1
        elif thalassemia == "Reversable Defect":
            thalassemia = 2
        elif thalassemia == "Fixed Defect":
            thalassemia = 3
        else:
            # Handle the case when an invalid value is selected
            st.write("Pilihan thalassemia tidak valid.")
        
        # Preprocess input data
        if slope == "Downsloping":
            slope = 0
        elif slope == "Flat":
            slope = 1
        elif slope == "Upsloping":
            slope = 2
        else:
            # Handle the case when an invalid value is selected
            st.write("Pilihan slope tidak valid.")
        
        
        input_data = [age, 0 if sex == "Pria" else 1, chest_pain_type, resting_blood_pressure, cholestoral,
                      1 if fasting_blood_sugar == "Lebih dari 120 mg/dl" else 0, rest_ecg, Max_heart_rate,
                      1 if exercise_induced_angina == "Ya" else 0, oldpeak, slope,
                      vessels_colored_by_flourosopy, thalassemia]
        input_scaled = preprocess_input(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)

        # Show prediction result
        if prediction[0] == 0:
            st.markdown("<h3 style='color: green;'>Hasil Prediksi: Tidak Terkena Penyakit Jantung</h3>", unsafe_allow_html=True)
            # st.write("Hasil Prediksi: Tidak Terkena Penyakit Jantung")
        else:
            # st.write("Hasil Prediksi: Terkena Penyakit Jantung")
            st.markdown("<h3 style='color: red;'>Hasil Prediksi: Terkena Penyakit Jantung</h3>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()

