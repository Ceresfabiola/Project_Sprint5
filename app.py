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

    # Creating the checkbox for the histogram
build_histogram = st.checkbox('Create Histogram')

if build_histogram:  # if the checkbox is selected
    # Display a message
    st.write('Creating a histogram for the car sales ads dataset')

    # Create the histogram
    fig = px.histogram(car_data, x="odometer")

    # Display the interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)

# Creating the checkbox for the scatter plot
build_scatter = st.checkbox('Create Scatter Plot')

if build_scatter:  # if the checkbox is selected
    # Display a message
    st.write('Creating a scatter plot for the car sales ads dataset')

    # Create the scatter plot
    fig = px.scatter(car_data, x="odometer", y='price')

    # Display the interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)
