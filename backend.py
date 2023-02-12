from requests import get
from os import getenv

WEATHER_API_KEY = getenv('WEATHER_API_KEY')


def get_weather_data(location, forecast_days_count, data_type):

    response = get('https://api.openweathermap.org/data/2.5/forecast', params={
        "q": location,
        "appid": WEATHER_API_KEY,
        # This API has temperature data every 3 hours for free account, so cnt = 8 means forecasting 1 day
        "cnt": forecast_days_count * 8
    }).json()

    if data_type == 'Temperature':
        filtered_data = [single_piece_of_data['main']['temp'] / 10 for single_piece_of_data in response['list']]
    else:
        filtered_data = [single_piece_of_data['weather'][0]['main'] for single_piece_of_data in response['list']]

    return filtered_data

