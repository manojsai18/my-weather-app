import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")   # Load environment variables from.env


BASE_URL ="http://api.openweathermap.org/data/2.5/weather"   # weather API base URL

 # Open WeathrMap Geocoding API endpoints

DIRECT_GEOCODE_URL ="http://api.openweathermap.org/geo/1.0/direct"
# For direct geocoding (city name to coords)
DIRECT_GEOCODE_WITH_ZIPCODE_URL ="http://api.openweathermap.org/geo/1.0/zip"
# For direct geocoding with (zipcode)

REVERSE_GEOCODE_URL ="http://api.openweathermap.org/geo/1.0/reverse"
# for reverse geocoding (coords to city name)




