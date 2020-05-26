import plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode()

def eda_timeseries(data, x, y):
    
    try:
        print("Distribution - Time Series Data")
        plot_title = "Distribution of "+y+" across "+x
        data = go.Scatter(x=data[x], y=data[y])
        layout = go.Layout(title=plot_title, xaxis=dict(title=x), yaxis=dict(title=y))
        fig = go.Figure(data=[data], layout=layout)
        plotly.offline.iplot(fig)
        
    except Exception as e:
        print(e)