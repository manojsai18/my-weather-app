from helper import direct_geocode,reverse_geocode, get_weather, format_weather, get_uv_index,get_current_location

def main():
    city = input("Enter city name (or leave blank for current location): ").strip()
    
    
    if city:
        location = direct_geocode(city)
        if not location:
            print("City not found. Please check the name and try again.")
            return
        lat, lon = location["lat"], location["lon"]
        print(f"\nWeather for {city}:")
    else:
        location= get_current_location()
        if not location:
            print( "not found")
            return
        location=direct_geocode(location)
        if not location:
            print("City not found. Please check the name and try again.")
            return
        lat, lon = location["lat"], location["lon"]
    print("\nWeather for your current location:")
    
    
    
    
    weather_data = get_weather(lat, lon)
    if not weather_data:
        print("Could not retrieve weather data.")
        return

    uv_index = get_uv_index(lat, lon,)
    
    print(format_weather(weather_data, uv_index))

if __name__ == "__main__":
    main()




