import requests
from datetime import datetime
from constants import WEATHER_API_KEY,BASE_URL,DIRECT_GEOCODE_URL,DIRECT_GEOCODE_WITH_ZIPCODE_URL,REVERSE_GEOCODE_URL

def get_current_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc")  # format: "lat,lon"
            if loc:
                lat, lon = map(float, loc.split(","))
                return lat, lon
    except Exception as e:
        print(f"Could not get current location: {e}")
    return None, None



def direct_geocode(city_name,limit=1):
    params = {
            "q": city_name,
            "limit": limit,
            "appid": WEATHER_API_KEY


    }


   #Get latitude and longitude for a city name using direct geocoding API.
    #Returns a dict with lat, lon if found, else None.
    

    response =requests.get(DIRECT_GEOCODE_URL,params=params)
    if response.status_code == 200:
        json_response = response.json()
        if json_response:  # Check if list is not empty
            data = json_response[0]
    return {"lat":data["lat"],"lon":data["lon"]}
    return None

def reverse_geocode(lat,lon,limit=1):
#Get location details (city, state, country) from lat, lon using reverse geocoding API.
     #Returns a dict with name and other details if found, else None.

    params = {
      "lat":lat,
      "lon":lon,
      "limit": limit,
      "appid":WEATHER_API_KEY

    }

    response = requests.get(REVERSE_GEOCODE_URL,params=params)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return {
            "name": data.get("name"),
            "state": data.get("state"),
            "country": data.get("country")
        }
    return None

def get_weather_by_coords(lat, lon):
    """
    Fetch weather data using latitude and longitude.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def get_weather_by_city(city):
    """
    Fetch weather data using city name.
    """
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def get_uv_index(lat, lon):
    """
    Fetch UV index for given coordinates.
    """
    uv_url = "http://api.openweathermap.org/data/2.5/uvi"
    params = {"lat": lat, "lon": lon, "appid": WEATHER_API_KEY}
    response = requests.get(uv_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("value")  # UV index value
    return None


def format_unix_time(unix_timestamp):
    """
    Convert Unix timestamp to readable local time string.
    """
    return datetime.fromtimestamp(unix_timestamp).strftime('%H:%M:%S')

def format_weather(data, uv_index=None):
    """
    Format weather data with UV index, sunrise, sunset times included.
    """
    if not data:
        return "Weather data not available."

    city = data.get("name")
    weather_desc = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    sunrise_unix = data["sys"]["sunrise"]
    sunset_unix = data["sys"]["sunset"]
    sunrise = format_unix_time(sunrise_unix)
    sunset = format_unix_time(sunset_unix)

    uv_text = f"{uv_index}" if uv_index is not None else "Not available"


    return (
        f"Weather in {city}:\n"
        f"Condition: {weather_desc}\n"
        f"Temperature: {temp}°C (feels like {feels_like}°C)\n"
        f"Humidity: {humidity}%\n"
        f"Sunrise: {sunrise}\n"
        f"Sunset: {sunset}\n"
        f"UV Index: {uv_text}"
    
    
    
    )





