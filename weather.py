import os
from dotenv import load_dotenv
from pprint import pprint
import requests

load_dotenv()

def get_current_weather(city="Abu Dhabi"):
    requests_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric"
    weather_data = requests.get(requests_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n ******** Get current weather conditions ***********\n")
    city = input("Enter city name: ")
    if not bool(city.strip()):
        city = "Abu Dhabi"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
