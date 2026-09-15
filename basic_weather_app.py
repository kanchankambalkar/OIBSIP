import requests

# Your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n----- Weather Report -----")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Feels like:", feels_like, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", description)

else:
    print("City not found or API key is invalid.")