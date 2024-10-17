import requests
from config.config import API_KEY, CITIES

def get_weather_data():
    weather_data = []
    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data.append(response.json())
    return weather_data
