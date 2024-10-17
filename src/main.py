import schedule
import time
from api_client import get_weather_data
from processor import process_weather_data
from alerts import check_alerts

UPDATE_INTERVAL = 5

def job():
    # Retrieve and process weather data
    print("Fetching weather data...")
    data = get_weather_data()
    process_weather_data(data)
    check_alerts(data)

if __name__ == "__main__":
    schedule.every(UPDATE_INTERVAL).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
