'''
Imp: check 'location' in main.
     replcae your api key with <YOUR_API>.
     If you are using another api then you have to modify API_ENDPOINT ,parse_temperature and parse_condition.
'''

import requests
API_KEY = "YOUR_API"
API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
def fetch_weather_data(location):
    params = {
        "appid": API_KEY,
        "q": location,
        "units": "metric"
    }
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()
    return data

def parse_temperature(weather_data):
    temperature = weather_data["main"]["temp"]
    return temperature

def parse_condition(weather_data):
    condition = weather_data["weather"][0]["description"]
    return condition

def main():
    location = <Enter_your_ZIP_code_here>
    weather_data = fetch_weather_data(location)

    if weather_data["cod"] == "404":
        print("Error: Location not found.")
    else:
        temperature = parse_temperature(weather_data)
        condition = parse_condition(weather_data)

        print("Temperature:", temperature, "°C")
        print("Condition:", condition)

if __name__ == "__main__":
    main()
