import plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()

def plot_time_series_distribution(data, datetime_column, target_column):
    plot_title = "Distribution of "+target_column+" across "+datetime_column
    data = go.Scatter(x=data[datetime_column], y=data[target_column])
    layout = go.Layout(title=plot_title, xaxis=dict(title='Date'), yaxis=dict(title=target_column))
    fig = go.Figure(data=[data], layout=layout)
    plotly.offline.iplot(fig)