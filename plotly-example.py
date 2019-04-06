import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# Create random data with numpy
import numpy as np
plotly.tools.set_credentials_file(username='conscript86', api_key='Frn32oku7wfN6podJfY2')
N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

py.plot(data, filename='basic-line')