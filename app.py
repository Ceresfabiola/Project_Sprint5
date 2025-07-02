import pandas as pd
import plotly.express as px
import streamlit as st

# Creating the header
st.header('Car Sales Explorer')

# Reading the data
car_data = pd.read_csv('vehicles.csv')

# Creating the button
hist_button = st.button('Create Histogram')

if hist_button:  # if the button is clicked
    # display a message
    st.write('Creating a histogram for the car sales ads dataset')

    # create a histogram
    fig = px.histogram(car_data, x="odometer")

    # display an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)

    # Creating the 2nd button
scatter_button = st.button('Create Scatter Plot')

if scatter_button:  # if the button is clicked
    # display a message
    st.write('Creating a scatter plot for the car sales ads dataset')

    # create a scatter plot
    fig = px.scatter(car_data, x="odometer", y='price')

    # display an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)
