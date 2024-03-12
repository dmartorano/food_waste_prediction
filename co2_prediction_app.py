from operator import mod
import streamlit as st
import pandas as pd
import pickle

def load_model():
  with open('models/co2_prediction_dt.pkl', 'rb') as f:
    prediction_model = pickle.load(f)
  return prediction_model

model = load_model()

st.title('How Much CO2 Does Our Food Produce?')

def get_data():
  return {"Consumption, tons": tons_consumed, 
          "Donation, tons": tons_donated, 
          "Biomaterial Processing, tons": tons_biomaterial_processing, 
          "Animal Feed, tons": tons_animal_feed,
          "Anaerobic Digestion, tons": tons_anaerobically_digested, 
          "Compost, tons": tons_composted, 
          "Land Application, tons": tons_land_application, 
          "Incineration, tons": tons_incinerated,
          "Landfill, tons": tons_landfilled, 
          "Sewer, tons": tons_sewer, 
          "Refused/Discarded, tons": tons_refuse_discards, 
          "Sector_Farm": 1 if sector == 'Farm' else 0,
          "Sector_Foodservice": 1 if sector == 'Foodservice' else 0,
          "Sector_Manufacturing": 1 if sector == 'Manufacturing' else 0,
          "Sector_Residential": 1 if sector == 'Residential' else 0,
          "Sector_Retail": 1 if sector == 'Retail' else 0,
          "Food_Type_Breads_and_Bakery": 1 if food_type == 'Breads and Bakery' else 0,
          "Food_Type_Dairy_and_Eggs": 1 if food_type == 'Dairy and Eggs' else 0,
          "Food_Type_Dry_Goods": 1 if food_type == 'Dry Goods' else 0,
          "Food_Type_Fresh_Meat_and_Seafood": 1 if food_type == 'Fresh Meat and Seafood' else 0,
          "Food_Type_Frozen": 1 if food_type == 'Frozen' else 0,
          "Food_Type_Prepared_Foods": 1 if food_type == 'Prepared Foods' else 0,
          "Food_Type_Produce": 1 if food_type == 'Produce' else 0,
          "Food_Type_Ready_to_Drink_Beverages": 1 if food_type == 'Ready-to-Drink Beverages' else 0}

tons_consumed = st.number_input('Consumption, tons', min_value=0, placeholder="0")
tons_donated = st.number_input('Donation, tons', min_value=0, placeholder="0")
tons_biomaterial_processing = st.number_input('Biomaterial Processing, tons', min_value=0, placeholder="0")
tons_animal_feed = st.number_input('Animal Feed, tons', min_value=0, placeholder="0")
tons_anaerobically_digested = st.number_input('Anaerobic Digestion, tons', min_value=0, placeholder="0")
tons_composted = st.number_input('Compost, tons', min_value=0, placeholder="0")
tons_land_application = st.number_input('Land Application, tons', min_value=0, placeholder="0")
tons_incinerated = st.number_input('Incineration, tons', min_value=0, placeholder="0")
tons_landfilled = st.number_input('Landfill, tons', min_value=0, placeholder="0")
tons_sewer = st.number_input('Sewer, tons', min_value=0, placeholder="0")
tons_refuse_discards = st.number_input('Refused/Discarded, tons', min_value=0, placeholder="0")

sector = st.selectbox('Sector', ['Farm', 'Foodservice', 'Manufacturing', 'Residential', 'Retail'])
food_type = st.selectbox('Food Type', ['Breads and Bakery', 'Dairy and Eggs', 'Dry Goods', 'Fresh Meat and Seafood', 'Frozen','Prepared Foods', 'Produce', 'Ready-to-Drink Beverages'])

if st.button("Compile info"):
  data = get_data()
  df = pd.DataFrame(data, index=[0])
  
# Extract features from dataframe
features = df.values

# Predict CO2 equivalent of dataframe using model
prediction = model.predict(features)

st.success(f'Predicted CO2 equivalent: {prediction}')


