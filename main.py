from streamlit import title, text_input, slider, selectbox, subheader, plotly_chart
from plotly.express import line

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

subheader(f'{data_type} for the next {num_days_ahead} days in {place}')

dates = ['2022-10-25', '2022-10-26', '2022-10-27']
temperature = [10, 11, 15]


figure = line(x=dates, y=temperature, labels={
    "x": "Dates",
    "y": "Temperature (C)"
})

plotly_chart(figure)

