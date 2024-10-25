""" In Class Activites"""

__author__ = "Amishi Mishra"


## 9/11/24
def get_weather_report() -> str:
    weather: str = input("What is the weather?")

    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")

    return weather
