from requests import get
from os import getenv

WEATHER_API_KEY = getenv('WEATHER_API_KEY')


def get_weather_data(location, forecast_days_count):
    response = get('https://api.openweathermap.org/data/2.5/forecast', params={
        "q": location,
        "appid": WEATHER_API_KEY,
        # This API has temperature data every 3 hours for free account, so cnt = 8 means forecasting 1 day
        "cnt": forecast_days_count * 8,
        # To change unit from Kelvin to Celsius
        "units": "metric"
    }).json()

    return response['list']


if __name__ == '__main__':
    print(get_weather_data('London', 5))
