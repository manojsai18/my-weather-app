import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.environ("WEATHER_API_KEY")   # Load environm=ent variables from.env


BASE_URL =https://api.openweathermap.org/data/3.0/onecall   # weather API base URL

 # Open WeathrMap Geocoding API endpoints

DIRECT_GEOCODE_URL =http://api.openweathermap.org/geo/1.0/direct?l={city name},{state code},{country code}&limit={limit}&appid={WEATHER_API_KEY}
# For direct geocoding (city name to coords)
DIRECT_GEOCODE_WITH_ZIPCODE_URL =http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={WEATHER_API_KEY}
# For direct geocoding with (zipcode)

REVERSE_GEOCODE_URL =http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={WEATHER_API_KEY}
# for reverse geocoding (coords to city name)

units:'metrics'



