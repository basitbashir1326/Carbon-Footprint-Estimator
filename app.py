import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and pipeline
model = joblib.load("carbon_model.pkl")
pipeline = joblib.load("carbon_pipeline.pkl")

st.title("🌱 Carbon Footprint Predictor")
st.write("Estimate your weekly CO₂ emissions based on your lifestyle.")

# User input
diet = st.selectbox("Diet", ["Vegan","pescatarian", "Vegetarian", "Omnivore"])
transport = st.selectbox(
    "Transport", ["private"]
)
electricity = st.number_input("Electricity Usage (kWh per week)", min_value=0.0)
vehicle_type = st.selectbox(
    "Vehicle Type", ["Petrol", "Diesel", "Electric", "Hybrid", "None"]
)
vehicle_distance = st.number_input("Vehicle Distance (km/month)", min_value=0.0)
heating = st.selectbox("Heating Energy Source", ["Electricity", "Gas", "Wood", "Coal"])

waste_bag_size = st.selectbox("Waste Bag Size", ["Small", "Medium", "Large"])
waste_bag_count = st.number_input("Waste Bag Weekly Count", min_value=0)
new_clothes = st.number_input("How Many New Clothes Monthly", min_value=0)
air_travel = st.selectbox("Frequency of Traveling by Air", ["Never", "Rarely", "Sometimes", "Often", "Very Often"])
energy_eff = st.selectbox("Energy Efficiency", ["Sometimes", "Yes", "No"])
internet_use = st.number_input("How Long Internet Daily (Hours)", min_value=0.0)
tv_pc_use = st.number_input("How Long TV/PC Daily (Hours)", min_value=0.0)
# Create input DataFrame
input_data = pd.DataFrame({
    "Diet": [diet],
    "Transport": [transport],
    "Electricity Usage (kWh)": [electricity],
    "Vehicle Type": [vehicle_type],
    "Vehicle Monthly Distance Km": [vehicle_distance],
    "Heating Energy Source": [heating],
    "Waste Bag Size": [waste_bag_size],
    "Waste Bag Weekly Count": [waste_bag_count],
    "How Many New Clothes Monthly": [new_clothes],
    "Frequency of Traveling by Air": [air_travel],
    "Energy efficiency": [energy_eff],
    "How Long Internet Daily Hour": [internet_use],
    "How Long TV PC Daily Hour": [tv_pc_use]
})


# Predict
if st.button("Predict CO₂ Footprint"):
    prediction = model.predict(input_data)
    st.success(f"🌍 Estimated Weekly CO₂ Emissions: **{int(prediction[0])} kg CO₂**")
