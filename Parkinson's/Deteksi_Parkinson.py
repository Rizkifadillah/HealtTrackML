# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 21:10:40 2023

@author: rizki
"""



import streamlit as st
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load model
model = joblib.load("D:/Data Science/Project/Healtcare/Parkinson's/model_parkinson.pkl")

# Load scaler
scaler = joblib.load("D:/Data Science/Project/Healtcare/Parkinson's/scaler_parkinson.pkl")

# Function to preprocess user input
def preprocess_input(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    return input_scaled

# Main function for Streamlit app
def main():
    # Set page title
    st.title("Deteksi Parkinson")


    # Create input fields for user
    mdvp_fo_hz = st.slider("MDVP-Fo(Hz)", 0.0, 300.0, 150.0)
    mdvp_fhi_hz = st.slider("MDVP-Fhi(Hz)", 0.0, 400.0, 200.0)
    mdvp_flo_hz = st.slider("MDVP-Flo(Hz)", 0.0, 200.0, 100.0)
    mdvp_jitter_percent = st.slider("MDVP-Jitter(%)", 0.0, 1.0, 0.02)
    mdvp_jitter_abs = st.slider("MDVP-Jitter(Abs)", 0.0, 0.01, 0.0002)
    mdvp_rap = st.slider("MDVP-RAP", 0.0, 0.05, 0.01)
    mdvp_ppq = st.slider("MDVP-PPQ", 0.0, 0.05, 0.015)
    jitter_ddp = st.slider("Jitter-DDP", 0.0, 0.1, 0.03)
    mdvp_shimmer = st.slider("MDVP-Shimmer", 0.0, 1.0, 0.05)
    mdvp_shimmer_db = st.slider("MDVP-Shimmer(dB)", 0.0, 1.0, 0.3)
    shimmer_apq3 = st.slider("Shimmer-APQ3", 0.0, 0.1, 0.015)
    shimmer_apq5 = st.slider("Shimmer-APQ5", 0.0, 0.1, 0.02)
    mdvp_apq = st.slider("MDVP-APQ", 0.0, 0.1, 0.025)
    shimmer_dda = st.slider("Shimmer-DDA", 0.0, 0.2, 0.045)
    nhr = st.slider("NHR", 0.0, 0.5, 0.01)
    hnr = st.slider("HNR", 0.0, 30.0, 15.0)
    rpde = st.slider("RPDE", 0.0, 1.0, 0.5)
    dfa = st.slider("DFA", 0.0, 2.0, 1.0)
    spread1 = st.slider("spread1", -10.0, 10.0, 0.0)
    spread2 = st.slider("spread2", 0.0, 10.0, 5.0)
    d2 = st.slider("D2", 0.0, 10.0, 3.0)
    ppe = st.slider("PPE", 0.0, 1.0, 0.5)

    # Create a button for prediction
    if st.button("Prediksi"):
        # Preprocess input data
        input_data = [mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_percent, mdvp_jitter_abs,
                      mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db,
                      shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr,
                      rpde, dfa, spread1, spread2, d2, ppe]
        input_scaled = preprocess_input(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)

        # Show prediction result
        if prediction[0] == 0:
            st.markdown("<h3 style='color: green;'>Hasil Prediksi: Tidak Terkena Parkinson's</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color: red;'>Hasil Prediksi: Terkena Parkinson's</h3>", unsafe_allow_html=True)


# Run the Streamlit app
if __name__ == "__main__":
    main()
