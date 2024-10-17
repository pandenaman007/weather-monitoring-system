# src/alerts.py

def check_alerts(weather_data, threshold=35):
    alerts = []

    for city_data in weather_data:
        city_name = city_data.get("name", "Unknown City")
        temperature_kelvin = city_data["main"]["temp"]
        # Convert Kelvin to Celsius only if the value is above 100 (or assume it's in Kelvin)
        temperature_celsius = temperature_kelvin - 273.15

        if temperature_celsius > threshold:
            alerts.append(f'ALERT: High temperature in {city_name}!')

    return alerts
