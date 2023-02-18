from streamlit import title, text_input, slider, selectbox, subheader, plotly_chart, image, write
from plotly.express import line
from time import localtime, strftime

from backend import get_weather_data

title('Weather forecast for the next days')

place = text_input('Place: ')

num_days_ahead = slider(
    'Forecast days ahead',
    min_value=1,
    max_value=5,
    help='Select the number of forecasted days'
)

data_type = selectbox(
    'Select data to view',
    ('Temperature', 'Sky Condition')
)


if place:
    try:
        subheader(f'{data_type} for the next {num_days_ahead} days in {place}')
        weather_data = get_weather_data(location=place, forecast_days_count=num_days_ahead)

        if data_type == 'Temperature':
            temperatures = [single_piece_of_data['main']['temp'] for single_piece_of_data in weather_data]
            dates = [single_piece_of_data['dt_txt'] for single_piece_of_data in weather_data]

            figure = line(x=dates, y=temperatures, labels={
                "x": "Dates",
                "y": "Temperature (C)"
            })

            plotly_chart(figure)

        else:
            sky_conditions = [single_piece_of_data['weather'][0]['main'] for single_piece_of_data in weather_data]

            image(
                image=[f'images/{single_sky_condition.lower()}.png' for single_sky_condition in sky_conditions],
                caption=[strftime('%a, %b-%d, %H %M', localtime(single_piece_of_data['dt'])) for single_piece_of_data in weather_data],
                width=115
            )
    except KeyError:
        write('The place you entered does not exist.')
