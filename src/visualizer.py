import matplotlib.pyplot as plt
import datetime


def plot_daily_summary(daily_summary):
    cities = daily_summary.keys()

    for city in cities:
        data = daily_summary[city]

        dates = [datetime.datetime.now()]  # Example date for now, adjust based on real data

        # Plot Average, Max, Min temperatures for the city
        plt.figure(figsize=(10, 6))
        plt.plot(dates, [data['average_temp']], label='Average Temp (°C)', color='blue', marker='o')
        plt.plot(dates, [data['max_temp']], label='Max Temp (°C)', color='red', marker='o')
        plt.plot(dates, [data['min_temp']], label='Min Temp (°C)', color='green', marker='o')

        # Customize chart
        plt.title(f"Daily Temperature Summary for {city}")
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid(True)

        # Show or save the plot
        plt.show()


def plot_historical_trends(weather_data):
    cities = weather_data.keys()

    for city in cities:
        data = weather_data[city]
        dates = [datetime.datetime.now() - datetime.timedelta(days=i) for i in range(len(data['temps']))]

        plt.figure(figsize=(10, 6))

        # Plot historical temperatures for the city
        plt.plot(dates, data['temps'], label='Temperature (°C)', color='blue', marker='o')

        # Customize chart
        plt.title(f"Historical Temperature Trends for {city}")
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.grid(True)

        plt.show()


def plot_alerts(alerts):
    if not alerts:
        print("No alerts to display.")
        return

    for alert in alerts:
        print(alert)
        # You can create custom visualizations for alerts if needed, but for now, we're just printing them.
