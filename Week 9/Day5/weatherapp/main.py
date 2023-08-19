import pyowm
import pytz
import matplotlib.pyplot as plt
from datetime import datetime

# OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
owm = pyowm.OWM(API_KEY)

# Function to get weather information for a location
def get_weather_info(location):
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    wind = w.get_wind()
    sunrise_time = pytz.utc.localize(datetime.utcfromtimestamp(w.get_sunrise_time()))
    sunset_time = pytz.utc.localize(datetime.utcfromtimestamp(w.get_sunset_time()))

    return {
        "temperature": w.get_temperature('celsius')["temp"],
        "humidity": w.get_humidity(),
        "wind": wind["speed"],
        "sunrise": sunrise_time.strftime("%H:%M:%S"),
        "sunset": sunset_time.strftime("%H:%M:%S")
    }

# Function to display weather information in a user-friendly way
def display_weather_info(weather_info):
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Wind Speed: {weather_info['wind']} m/s")
    print(f"Sunrise: {weather_info['sunrise']}")
    print(f"Sunset: {weather_info['sunset']}")

# Function to get the weather forecast for a location
def get_weather_forecast(location):
    forecast = owm.three_hours_forecast(location)
    return forecast.get_forecast().get_weathers()

# Function to display the weather forecast
def display_weather_forecast(forecast):
    for weather in forecast:
        print(f"Time: {weather.get_reference_time('iso')} | Temperature: {weather.get_temperature('celsius')["temp"]}°C")

# Function to plot the humidity bar chart
def plot_humidity_forecast(humidity_data):
    dates = [date for date, _ in humidity_data]
    humidity = [value for _, value in humidity_data]
    
    plt.bar(dates, humidity)
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title('Three-day Humidity Forecast')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Get current weather information for a location
    location = input("Enter the location: ")
    weather_info = get_weather_info(location)
    print("Current Weather Information:")
    display_weather_info(weather_info)

    # Get and display weather forecast
    forecast = get_weather_forecast(location)
    print("\nWeather Forecast:")
    display_weather_forecast(forecast)

    # Plot humidity forecast bar chart (Bonus)
    humidity_data = [(weather.get_reference_time('iso'), weather.get_humidity()) for weather in forecast[:3]]
    plot_humidity_forecast(humidity_data)

if __name__ == "__main__":
    main()
