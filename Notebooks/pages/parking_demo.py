import pandas as pd
import streamlit as st
import joblib
import numpy as np
from geopy.geocoders import Nominatim
import altair as alt
import folium

#######################################################################################################################################
### set title and load data
st.title("ParkSmart 🚗")

@st.cache_data 
def load_data(path, num_rows):
    df = pd.read_csv(path, nrows=num_rows)
    return df

# load data
df = load_data("../data/parking_coord.csv", 1700000)
# df_5 = load_data("../data/parking_coord_5_rows.csv", 5)
# st.write('Here are the first few rows of Toronto\'s Parking Ticket data from 2016 to 2022')
# st.dataframe(df_5)

#######################################################################################################################################
### Model
st.write('''
        Introducing ParkSmart, your ultimate parking pal in the urban jungle. 
        Simply enter your destination, and it displays a maze of parking regulations, 
        showing you which violations lurk in the shadows of your chosen address. But that's not all – 
        ParkSmart also sheds light on peak parking times. Start parking worry free!
''')
#function to retrieve prediction
def get_pred_output(latitude, longitude):
    input_pred = np.array([[latitude, longitude]])

    prediction = model.predict(input_pred)
    indices = np.where(prediction == 1)
    fine_amounts = df.iloc[indices[0]]['set_fine_amount']
    labels = infraction_types.columns[indices[1]]

    
    return fine_amounts,labels

def generate_map(address):
    geolocator = Nominatim(user_agent="toronto-parking-application")
    location = geolocator.geocode(address, timeout=10)
    if location is not None:
        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)
        folium.Marker([location.latitude, location.longitude], popup=address).add_to(m)
        return m
    else:
        st.write("Address does not exist.")

#get model
model = joblib.load('../Model/model_custom_best(2).pkl')

option = st.selectbox('Select an option or enter your own address.', ['3042 Dundas St W', '4700 Keele St', '21 Hillcrest Ave', '60 St Patrick St', '692 Shaw St', '441 Rogers Rd', 'Enter your own address'])

# If the selected option is 'Enter your own address', display a text input
if option == 'Enter your own address':
    text = st.text_input('Enter your address text below. Use street, west, avenue as (st, w, ave). \n\n An address with no unit number may give multiple predictions.', '4700 Keele St')
else:
    text = option

#changes address to adhere to database context
text_with_location = text.upper() + ', TORONTO, ON, CANADA'

# Placeholder for output
output_placeholder = st.empty()

infraction_types = df[['permit_time_restrictions', 'fee_related', 'time_related', 'fire_route', 'accessible_related', 'commercial_related', 'obstruction_related', 'cycle_related']]

def infraction_desc(labels):
    descriptions = {
        "permit time restrictions": "These violations include parking on private property without authorization, parking in prohibited areas or during restricted times indicated by signage, failure to display a required parking permit, and parking outside permitted timeframes or areas designated for specific permits. ",
        "fee related": "Fee Related parking tickets include instances where required fees are not paid, such as failing to activate a parking meter, neglecting to deposit a fee in the meter, or parking without paying for the allotted time. Additionally, violations occur when a parking receipt is not displayed, or when parking at an expired meter.",
        "time related": "These violations are related to time constraints and regulations. It includes exceeding specified parking durations, parking outside designated periods, stopping in pedestrian zones, parking outside marked spaces, failing to activate parking meters, and stopping in areas with restricted time or day regulations.",
        "fire route": "Violations related to parking in or near fire routes and fire hydrants. Offenses include parking within designated fire routes, within a certain distance of fire hydrants, or in areas marked for emergency vehicle access. Violations range from parking too close to a fire hydrant to obstructing fire halls on opposite or same sides of the street.",
        "accessible related": "These violations include parking or standing in accessible zones without a permit, stopping in areas designated for accessible parking without authorization, and obstructing snow routes or railway tracks. Additionally, the tickets encompass unauthorized parking or stopping in designated handicapped spaces, as well as loading or unloading in accessible areas without the required permit.",
        "commercial related": "These violations include parking in designated commercial loading zones without authorization and parking or leaving a vehicle in areas reserved for buses or shared vehicle waiting areas. Some of these violations can disrupt traffic flow, impede on public transportation services, and obstruct designated areas that are intended for commercial activities.",
        "obstruction related": "These violations include parking or stopping in areas that block driveways, laneways, or ramps; failing to park or stop parallel to the curb as required; parking outside of designated spaces or areas; transit stops, or roadside stops; and parking too close to intersections or pedestrian crossings. It could also involve parking on boulevards, front yards, or in areas not designated for parking.",
        "cycle related": "Cycle violations is related to the misuse of bicycle lanes and spaces by non-bicycle vehicles or improper parking of motorcycles. Violations include stopping non-bicycle vehicles in designated cycle tracks, parking non-motorcycles in motorcycle spaces, parking vehicles on bicycle paths, and improper parking of motorcycles at specific angles exceeding the designated limits."
    }
    description_str = ""
    for label in labels:
        description_str += descriptions[label.replace('_', ' ')] + '\n'
    return description_str

#if input address in dataframe
if text_with_location in df['location2'].values:
    output_placeholder.write('running...')
    matched_rows = df[df['location2'] == text_with_location]
    if not matched_rows.empty:
        offence = ""
        matched_row = matched_rows.iloc[0]
        latitude = matched_row['latitude']
        longitude = matched_row['longitude']
        fine_amount = matched_row['set_fine_amount']
        fine_amounts, labels = get_pred_output(latitude, longitude)
        output_text = ""

        #output of prediction
        for label in labels:
            offence = label
            output_text += f"This model predicts a '{offence.replace('_', ' ')}' parking ticket for this location with a fine of ${fine_amount}."
        output_placeholder.write(output_text)   

        #description of infraction
        descriptions = infraction_desc(labels)
        formatted_labels = [label.replace('_', ' ').capitalize() for label in labels]

        # Display each formatted label as a subheader
        for formatted_label in formatted_labels:
            st.subheader(formatted_label)
        st.write(f"{descriptions}")

        #map of address
        st.subheader(f"Map of {text.upper()}") 
        st.map(data = matched_rows, size=8, color="#639cd9", latitude = latitude, longitude = longitude, zoom=15) 

        #peak time bar chart
        # Define hour categories
        hour_categories = {
            0: '00:00', 1: '01:00', 2: '02:00', 3: '03:00',
            4: '04:00', 5: '05:00', 6: '06:00', 7: '07:00',
            8: '08:00', 9: '09:00', 10: '10:00', 11: '11:00',
            12: '12:00', 13: '13:00', 14: '14:00', 15: '15:00',
            16: '16:00', 17: '17:00', 18: '18:00', 19: '19:00',
            20: '20:00', 21: '21:00', 22: '22:00', 23: '23:00'
        }
        
        st.subheader(f"Peak Times for {text.upper()}")
        df['datetime_of_infraction'] = pd.to_datetime(df['datetime_of_infraction'])
        loc_peak_time = df[df['location2'] == text_with_location].groupby(df['datetime_of_infraction'].dt.hour).size().reset_index(name='count')

        hourly_peak_time_chart = pd.DataFrame({
            'Hour': [hour_categories[hour] for hour in loc_peak_time['datetime_of_infraction']],
            'Number of Tickets': loc_peak_time['count']
        })
        # Create Altair bar chart
        chart = alt.Chart(hourly_peak_time_chart).mark_bar(color="#639cd9").encode(
            x=alt.X('Hour', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('Number of Tickets')
        )

        # Display the chart
        st.altair_chart(chart, use_container_width=True)

else:
    geolocator = Nominatim(user_agent="toronto-parking-application")
    location = geolocator.geocode(text_with_location, timeout=10)
    offence = ""
    if location.latitude is None:
        st.write("Address does not exist.")
    else:
        fine_amounts, labels = get_pred_output(location.latitude, location.longitude)
    
        output_text = ""
        for fine_amount, label in zip(fine_amounts, labels):
            offence = label
            output_text += f"This model predicts a '{offence.replace('_', ' ')}' parking ticket for this location area with a fine of ${fine_amount}."

        #description of infraction
        descriptions = infraction_desc(labels)
        formatted_labels = [label.replace('_', ' ').capitalize() for label in labels]
        for formatted_label in formatted_labels:
            st.subheader(formatted_label)
        st.write(f"{descriptions}")

        output_placeholder.write(output_text) 
        
        st.subheader(f"Map of the  {text.upper()}:")
        folium_map = generate_map(text_with_location)
        if folium_map is not None:
            folium_map.save("map.html")
            st.components.v1.html(open("map.html", "r").read(), width=700, height=500)

#######################################################################################################################################
###  Sidebar Info 
st.sidebar.caption('Linkedin')
st.sidebar.write('👥 linkedin.com/tilovashahrin')

st.sidebar.caption('Github')
st.sidebar.write('🖥️  github.com/tilovashahrin')
