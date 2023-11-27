import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)



# title of the sidebar
html_temp = """
<div style="background-color:lightblue;padding:10px">
<h2 style="color:black;text-align:center;">Car's Features </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)


# title of the body
html_temp = """
<div style="background-color:lightblue;padding:10px">
<h2 style="color:black;text-align:center;">Car Price Predictor App</h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

#sidebar subhidder
st.sidebar.subheader('You can select the car features to see its price:')

# Set the sidebar car image
car_image = Image.open("blue-car-logo-png.webp")
st.sidebar.image(car_image, use_column_width=True)


car_image_2 = Image.open("icon-3418201_1280.png")
st.image(car_image_2, use_column_width=True) 

import pickle
filename = "rf2_model"
model=pickle.load(open(filename, "rb"))

# To take feature inputs
age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3))
hp_kW=st.sidebar.slider("What is the hp_kw of your car?", 40, 300, step=5)
Gears=st.sidebar.slider("What is the Gears of your car?", 5,8, step=1)
Gearing_Type=st.sidebar.radio('Select gear type',('Automatic','Manual','Semi-automatic'))
make_model=st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))
km=st.sidebar.slider("What is the km of your car", 0,350000, step=1000)
Weight_kg=st.sidebar.slider("What is the Weight in kg of your car?", 840, 2471, step=5)


# Create a dataframe using feature inputs
my_dict = {"age":age,
           "hp_kW":hp_kW,
           "Gears":Gears,
           "Gearing_Type":Gearing_Type,
           "make_model":make_model,
           "km": km,
           "Weight_kg":Weight_kg}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])