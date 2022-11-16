import requests

API_KEY = "ac79e3ae09bc111a8f43be1a1899d920"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=imperial"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    ftemperature = round(data["main"]["temp"])
    ctemperature = round((data["main"]["temp"] - 32) * 5/9)

    print("Weather:", weather)
    print("Temperature:", ftemperature, "Fahrenheit")
    print("Temperature:", ctemperature, "celsius")
else:
    print("An error occurred.")