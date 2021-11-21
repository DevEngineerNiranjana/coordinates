import pandas as pd
import plotly_express as px
from geopy.geocoders import Nominatim

# read the lat and lon values from csv file in to a dataframe.
# find, out of line coordinates and remove it from the dataframe and plot it in the map
try:
    locator = Nominatim(user_agent='myGeocoder')
    df = pd.read_csv("latitude_longitude_details.csv")
    for i, v in df.iterrows():
        coordinates = str(v["latitude"]) + "," + str(v["longitude"])
        location = locator.reverse(coordinates)
        if str(location.raw["osm_type"]) == "node":
            df.drop(i)
    fig = px.scatter_mapbox(df, lat='latitude', lon='longitude',

                            color_discrete_sequence=["red"],
                            zoom=13,
                            height=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()

except Exception as err:
    err_msg = "Exception : " + str(err)
    print(err_msg)
