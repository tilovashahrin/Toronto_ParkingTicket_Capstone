import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap

#######################################################################################################################################
### Create a title and load data

st.title("ParkSmart: Anticipating Toronto's Parking Tickets")
st.subheader("Insights from Toronto's Parking Ticket Data")

@st.cache_data 
def load_data(path, num_rows):
    df = pd.read_csv(path, nrows=num_rows)
    return df

# load data
df = load_data("../data/parking_coord.csv", 1755214)
st.write('Here are the first few rows of Toronto\'s Parking Ticket data from 2016 to 2022')
st.dataframe(df.head())

#######################################################################################################################################
### Describing the dataset
st.subheader("City of Toronto's Parking Enforcement")
st.write("The Parking Enforcement Unit of Toronto Police Service (TPS) is responsible for parking enforcement throughout City of Toronto in order to maintain smooth traffic flow and ensure public safety. TPS itself issued the majority of parking tickets, but there are still 9% tickets are issued by trained municipal law enforcement managers, who are private agency employees that are trained and certified by TPS for parking enforcement at City of Toronto. Currently, there are approximately 2,500 trained municipal law enforcement managers working for 115 different agencies. (City of Toronto, 2013)")


#######################################################################################################################################
### Model Description
model_desc = '''By analyzing historical data on parking tickets issued across the city, 
my model leverages advanced machine learning algorithms to identify patterns and trends associated with different 
types of parking violations. With this model, residents can make more informed decisions about where and how they park their vehicles. 
This knowledge empowers them to avoid potential violations, and reducing the likelihood of receiving costly fines and penalties. '''

st.subheader("Predictive Model")
st.write(model_desc)


st.subheader("Exploratory Data Analysis")
#######################################################################################################################################
### Create a map
st.write("All Parking Tickets in Toronto")
st.map(df, size=7, color="#639cd9")   

#######################################################################################################################################
### Create EDAs

### EDA 1
st.subheader('Total Revenue by Year')
st.write("The city made a whopping $17 Million CAD in 2016.")
filtered_df = df.groupby('year')['set_fine_amount'].sum()
filtered_chart = pd.DataFrame({
    'Year': filtered_df.index,
    'Amount ($)': filtered_df.values
})

# Convert 'Year' column to categorical
filtered_chart['Year'] = pd.Categorical(filtered_chart['Year'].astype(str), categories=filtered_chart['Year'].astype(str).sort_values(), ordered=True)

chart1 = alt.Chart(filtered_chart).mark_bar(color="#639cd9").encode(
    x=alt.X('Year', sort=alt.EncodingSortField(field="Year", order='ascending'), axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('Amount ($)')
)
st.altair_chart(chart1, theme='streamlit', use_container_width=True)

### EDA 2
st.subheader('Monthly Offences')
st.write('March and October are peak times for enforcement.')

month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

monthly_offences = df.groupby(df['month']).size()
monthly_offences_chart = pd.DataFrame({
    'Month': [month_names[month] for month in monthly_offences.index],
    'Count of Tickets': monthly_offences.values
})
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthly_offences_chart['Month'] = pd.Categorical(monthly_offences_chart['Month'], categories=month_order, ordered=True)

chart2 = alt.Chart(monthly_offences_chart).mark_bar(color="#639cd9").encode(
    x=alt.X('Month', axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('Count of Tickets')
)
st.altair_chart(chart2, theme='streamlit', use_container_width=True)

df_sampled = df.iloc[::2000]
chart3 = alt.Chart(df_sampled).mark_rect().encode(
    x=alt.X('longitude:Q', bin=True),
    y=alt.Y('latitude:Q', bin=True),
    color=alt.Color('count():Q', scale=alt.Scale(scheme='viridis'))
).properties(
    width=800,
    height=600,
    title='Density of Parking Infractions Across Toronto'
)

st.altair_chart(chart3, theme='streamlit', use_container_width=True)

#######################################################################################################################################
###  Sidebar Info 
st.sidebar.caption('Linkedin:')
st.sidebar.write('📧: linkedin.com/tilovashahrin')