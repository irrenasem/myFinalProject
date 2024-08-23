import requests
import sys
from datetime import datetime

API_KEY = '572860ae77c8dae0205bbd51f8cde237'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5'

def get_weather(city_name, date=None):
    # Construct the URL for current weather
    url = f'{BASE_URL}/weather?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Current weather in {city_name}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print(f"Error: {response.status_code}")
        return
    
    if date:
        # Construct the URL for future weather (7 days forecast)
        url = f'{BASE_URL}/forecast?q={city_name}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data['list']:
                dt = datetime.fromtimestamp(item['dt'])
                if dt.date() == datetime.strptime(date, '%Y-%m-%d').date():
                    print(f"\nWeather forecast for {city_name} on {date}:")
                    print(f"Temperature: {item['main']['temp']}°C")
                    print(f"Weather: {item['weather'][0]['description']}")
                    return
            print("No forecast data available for the given date.")
        else:
            print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_app.py <city_name> [<future_date>]")
        sys.exit(1)
    city_name = sys.argv[1]
    future_date = sys.argv[2] if len(sys.argv) > 2 else None
    get_weather(city_name, future_date)
