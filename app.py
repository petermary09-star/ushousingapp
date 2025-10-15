import joblib
import streamlit as st
import numpy as np

Housing_model = joblib.load('data_modell.pkl')


st.title('USA Housing Prediction App')
st.write('This app predicts the house pricing in selected area in USA based on given conditions')

st.subheader('Price of house to provided conditions')

Avg_Area_Income = st.sidebar.number_input('Average Area Income', 35000, 150000)
Avg_Area_House_Age = st.sidebar.select_slider('Select house age between 1 and 10', options=[1,2,3,4,5,6,7,8,9,10])
Avg_Area_number_of_rooms = st.sidebar.select_slider('Select the number of rooms between 4 and 15', options=[4,6,7,9,11,12,14,15])
Avg_Area_number_of_bedrooms = st.sidebar.select_slider('Select the average number of bedrooms between 1 and 6', options=[1,2,3,4,5,6])
Area_population = st.sidebar.number_input('Area Population', 10000, 95000)

input = np.array([Avg_Area_Income,Avg_Area_House_Age,Avg_Area_number_of_rooms,Avg_Area_number_of_bedrooms,Area_population]).reshape(1, -1)

result = Housing_model.predict(input)

if st.button('Predict'):
    st.write(f"The Price is: {result}")


