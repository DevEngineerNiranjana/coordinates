from geopy.geocoders import Nominatim
import pandas as pd

locator = Nominatim(user_agent='myGeocoder')
df = pd.read_csv("latitude_longitude_details.csv")
for i, v in df.iterrows():
    coordinates = str(v["latitude"]) + "," + str(v["longitude"])
    location = locator.reverse(coordinates)
    print(location.raw)
