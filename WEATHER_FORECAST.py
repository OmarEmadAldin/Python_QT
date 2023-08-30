import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] == 200:
        weather_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    else:
        return None

def main():
    api_key = 'YOUR_API_KEY'
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
