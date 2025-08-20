from helper import direct_geocode,reverse_geocode, get_weather_by_coords, format_weather, get_uv_index

def main():
    city = input("Enter city name: ").strip()
    if not city:
        print("Please enter a valid city name.")
        return

    location = direct_geocode(city)
    if not location:
        print("City not found. Please check the name and try again.")
        return

    lat, lon = location["lat"], location["lon"]
    weather_data = get_weather_by_coords(lat, lon)
    if not weather_data:
        print("Could not retrieve weather data.")
        return

    uv_index = get_uv_index(lat, lon)
    
    print(format_weather(weather_data, uv_index))

if __name__ == "__main__":
    main()




