from streamlit import title, subheader, selectbox, plotly_chart
from pandas import read_csv
from plotly.express import scatter

data_frame = read_csv('happy.csv')

title('In search for Happiness')

x_axis = selectbox(
    'Select the data for the X-axis',
    ('GDP', 'Happiness', 'Generosity')
)

y_axis = selectbox(
    'Select the data for the Y-axis',
    ('GDP', 'Happiness', 'Generosity')
)

subheader(f'{x_axis} and {y_axis}')

figure = scatter(
    data_frame=data_frame,
    x=x_axis.lower(),
    y=y_axis.lower(),
    labels={
        x_axis.lower(): x_axis,
        y_axis.lower(): y_axis
    }
)

plotly_chart(figure)
