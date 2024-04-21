import altair as alt
import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap

#######################################################################################################################################
### Create a title and load data

st.title("ParkSmart: Anticipating Toronto's Parking Tickets")
st.subheader("Insights from Toronto's Parking Ticket Data")

@st.cache_data 
def load_data(path, num_rows):
    df = pd.read_csv(path, nrows=num_rows)
    return df

# load data 1755214
df = load_data("../data/parking_df.csv", 12900000)
st.write('Here are the first few rows of Toronto\'s Parking Ticket data from 2016 to 2022')
st.dataframe(df.head())
df_coord = df[df['latitude'] != 0]
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
st.map(df_coord, size=7, color="#639cd9")   

#######################################################################################################################################
### Create EDAs

### EDA 1
st.subheader('Total Revenue by Year')
st.write("The city made a whopping $100 Million CAD in 2016.")
filtered_df = load_data("../data/total_fine_year.csv", 7)
filtered_chart = pd.DataFrame({
    'Year': filtered_df.iloc[:7, 0],
    'Amount ($)': filtered_df.iloc[:7, 1]
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

df_sampled = df_coord.iloc[::2000]
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

#chart 4
df['datetime_of_infraction'] = pd.to_datetime(df['datetime_of_infraction'])

# Filter data for the year 2022
df_2022 = df[df['datetime_of_infraction'].dt.year == 2022]
df_2022['hour'] = df['datetime_of_infraction'].dt.hour

# Define hour categories
hour_categories = {
    0: '00:00', 1: '01:00', 2: '02:00', 3: '03:00',
    4: '04:00', 5: '05:00', 6: '06:00', 7: '07:00',
    8: '08:00', 9: '09:00', 10: '10:00', 11: '11:00',
    12: '12:00', 13: '13:00', 14: '14:00', 15: '15:00',
    16: '16:00', 17: '17:00', 18: '18:00', 19: '19:00',
    20: '20:00', 21: '21:00', 22: '22:00', 23: '23:00'
}

# Categorize hours into time ranges
df_2022['hour_category'] = df_2022['hour'].map(hour_categories)

# Group by hour category and count infractions
infraction_hour = df_2022.groupby('hour_category').size().reset_index(name='count')

chart4 = alt.Chart(infraction_hour).mark_bar(color="#639cd9").encode(
    x=alt.X('hour_category:O', title='Hour of Day',  axis=alt.Axis(labelAngle=-45)),
    y=alt.Y('count:Q', title='Number of Tickets')
).properties(
    width=600,
    height=400
)
st.subheader('Peak Time for Ticketing (2022)')
st.altair_chart(chart4, use_container_width=True)

#######################################################################################################################################
###  Sidebar Info 
st.sidebar.caption('Linkedin:')
st.sidebar.write('👥 linkedin.com/tilovashahrin')

st.sidebar.caption('Github:')
st.sidebar.write('🖥️  github.com/tilovashahrin')
