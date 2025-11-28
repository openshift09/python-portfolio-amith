import requests

API_KEY = "b3797df91aa32b31622e92304a823713"  # Replace with your actual OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\n------ WEATHER REPORT ------")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Weather:", data["weather"][0]["description"])
            print("Humidity:", data["main"]["humidity"], "%")
            print("Wind Speed:", data["wind"]["speed"], "m/s")
            print("----------------------------\n")
        else:
            print("Error:", data.get("message", "Unable to fetch weather"))
    except Exception as e:
        print("Something went wrong:", str(e))


print("------ PYTHON WEATHER APP ------")

while True:
    city = input("Enter city name (or 'exit' to quit): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break

    get_weather(city)
