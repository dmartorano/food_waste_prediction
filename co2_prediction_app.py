from operator import mod
import streamlit as st
import pickle

def load_model():
  with open('models/co2_prediction.pkl', 'rb') as f:
    prediction_model = pickle.load(f)
  return prediction_model

model = load_model()

st.title('How Much CO2 Does Our Food Produce?')

sector = st.selectbox('Sector', [])