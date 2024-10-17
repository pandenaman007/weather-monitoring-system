def process_weather_data(weather_data):
    # This function processes weather data to compute rollups and aggregates
    processed_data = {}

    for entry in weather_data:
        city = entry["name"]
        temp = entry["main"]["temp"]
        condition = entry["weather"][0]["main"]

        if city not in processed_data:
            processed_data[city] = {
                "temps": [],
                "conditions": [],
            }

        processed_data[city]["temps"].append(temp)
        processed_data[city]["conditions"].append(condition)

    # Calculate aggregates for each city
    for city, data in processed_data.items():
        temps = data["temps"]
        conditions = data["conditions"]
        processed_data[city] = {
            "average_temp": sum(temps) / len(temps),
            "max_temp": max(temps),
            "min_temp": min(temps),
            "dominant_condition": max(set(conditions), key=conditions.count)
        }

    return processed_data


def calculate_daily_summary(weather_data):
    # This function calculates daily summaries of the weather data
    return process_weather_data(weather_data)
