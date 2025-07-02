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
    fig = px.histogram(car_data, x="odometer",
                       title='Distribution of Odometer Readings')

    # display an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)

    # Creating the 2nd button
scatter_button = st.button('Create Scatter Plot')

if scatter_button:  # if the button is clicked
    # display a message
    st.write('Creating a scatter plot for the car sales ads dataset')

    # create a scatter plot
    fig = px.scatter(car_data, x="odometer", y='price',
                     title='Relationship Between Odometer Readings and Car Prices')

    # display an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)

st.title('Car Sales Ads Data Explorer')
st.write('Select the charts you want to display:')

# Checkbox for price histogram
if st.checkbox('Show Price Histogram'):
    st.write('### Price Distribution')
    fig = px.histogram(car_data, x="price", title='Distribution of Car Prices')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox for model year histogram
if st.checkbox('Show Model Year Histogram'):
    st.write('### Model Year Distribution')
    fig = px.histogram(car_data, x="model_year",
                       title='Distribution of Car Model Years')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox for days listed histogram
if st.checkbox('Show Days Listed Histogram'):
    st.write('### Days Listed Distribution')
    fig = px.histogram(car_data, x="days_listed",
                       title='Distribution of Days Listed')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox for car condition histogram
if st.checkbox('Show Car Condition Histogram'):
    st.write('### Car Condition Distribution')
    fig = px.histogram(car_data, x="condition",
                       title='Distribution of Car Conditions')
    st.plotly_chart(fig, use_container_width=True)
