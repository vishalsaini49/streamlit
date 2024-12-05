import pandas as pd
import streamlit as st
import datetime
import pickle
import sklearn
import numpy as np

st.write(
    """
     # Cars24 Used Car Price Prediction
    """
)

encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


def model_pred(year, seller_type, km_driven, fuel_type, transmission_type, mileage, engine, max_power, seats):
    ## loading the model
    with open("D:\SCALER CLASSES\Github Desktop\streamlit\car_pred", 'rb') as file:
        reg_model = pickle.load(file)
        input_features = [[year, seller_type, km_driven, fuel_type, transmission_type, mileage, engine, max_power, seats]]

        return reg_model.predict(input_features)

## Formatting and adding dropdowns and sliders
col1, col2, col3 = st.columns(3)

year = col1.number_input("Enter the Make Year")
km_driven = col2.number_input("Enter the Driven_KM")
mileage = col3.number_input("Enter the Milage")

col4, col5, col6 = st.columns(3)
seller_type = col4.selectbox("Select the seller type", ['Dealer', 'Individual', 'Trustmark Dealer'])
fuel_type = col5.selectbox("Select the fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
transmission_type = col6.selectbox("Select the transmission type", ["Manual", "Automatic"])

col7, col8, col9 = st.columns(3)
engine = col7.slider("Set the Engine Power", 500, 5000, step=100)
max_power = col8.number_input("Enter the Max Power")
seats = col9.selectbox("Enter the number of seats", [4,5,7,9,11])

if (st.button("Predict Price")):
    seller_type = encode_dict['seller_type'][seller_type]
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(year, seller_type, km_driven, fuel_type, transmission_type, mileage, engine, max_power, seats)
    st.text("Predicted Price of the car is: " + str(np.round(price,2))+" Lakhs")