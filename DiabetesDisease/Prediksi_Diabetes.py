# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:29:03 2023

@author: rizki
"""

import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler


# Load model
model = pickle.load(open('D:/Data Science/Course Langing/Part 16 - Siddhardhan tutorial/Deploy Project/diabetes_model.pkl', 'rb'))

# Load scaler
scaler = pickle.load(open('D:/Data Science/Course Langing/Part 16 - Siddhardhan tutorial/Deploy Project/scaler.pkl', 'rb'))


#load_model_diabetes = load_model('D:/Data Science/Course Langing/Part 16 - Siddhardhan tutorial/Deploy Project/diabetes_model.sav')

def predict_diabetes(input_data):
    # Ubah input menjadi array numpy
    input_data_np = np.array(input_data).reshape(1, -1)
  
    # Standarisasi data
    input_data_scaled = scaler.transform(input_data_np)
  
    # Lakukan prediksi
    prediction = model.predict(input_data_scaled)
  
    return prediction[0]


def main():
    # Judul aplikasi
    st.title("Prediksi Diabetes")

    # Input fitur-fitur
    Pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=20, value=0)
    Glucose = st.slider("Kadar Glukosa", min_value=0, max_value=200, value=100)
    BloodPressure = st.slider("Tekanan Darah", min_value=0, max_value=150, value=70)
    SkinThickness = st.slider("Ketebalan Kulit", min_value=0, max_value=100, value=20)
    Insulin = st.slider("Insulin", min_value=0, max_value=500, value=50)
    BMI = st.slider("Indeks Massa Tubuh (BMI)", min_value=0.0, max_value=60.0, value=25.0)
    DiabetesPedigreeFunction = st.slider("Silsilah Diabetes", min_value=0.0, max_value=3.0, value=0.5)
    Age = st.number_input("Usia", min_value=0, max_value=150, value=30)

    # Prediksi ketika tombol ditekan
    if st.button("Prediksi"):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        prediction = predict_diabetes(input_data)

        if prediction == 0:
            st.markdown("<h3 style='color: green;'>Prediksi: Tidak Diabetes</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color: red;'>Prediksi: Diabetes</h3>", unsafe_allow_html=True)



if __name__ == '__main__':
    main()

