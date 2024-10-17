def check_alerts(weather_data):
    print("Checking alerts...")
    for city_data in weather_data:
        city = city_data["name"]
        temperature_celsius = city_data["main"]["temp"] - 273.15
        print(f"Temperature in {city}: {temperature_celsius:.2f}°C")  # Debug print

        if temperature_celsius > 35:
            print(f"ALERT: High temperature in {city}!")
        else:
            print(f"Temperature in {city} is normal.")
