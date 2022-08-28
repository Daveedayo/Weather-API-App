import requests

API_KEY = "e6187d9eced2f727340432205e27083d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    #weather = data['weather']
else:
    print("An error occurred")