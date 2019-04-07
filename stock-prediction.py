import pandas as pd
import numpy as np
from sklearn.svm import SVR
import plotly.plotly as py
import plotly.graph_objs as go

def get_data(filename):
    global dates
    global prices
    dtypes = {'date': 'str', 'close': 'float'}
    parse_dates = ['date']
    df = pd.read_csv(filename, dtype=dtypes, parse_dates=parse_dates)
    dates=df['date'].dt.strftime('%d').astype(int).tolist()
    prices=df['close'].tolist()
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1

    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1) # defining the support vector regression models
    svr_rbf.fit(dates, prices) # fitting the data points in the models
    svr_lin = SVR(kernel='linear', C=1e3, gamma='auto')
    svr_lin.fit(dates, prices)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2, gamma='auto')
    svr_poly.fit(dates, prices)

    layout = dict(title = 'Main Source for News',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Price'),
              )
    # Create and style trace
    values = go.Scatter(
        x = dates,
        y = prices,
		name = 'Values',
        mode = 'markers'
    )	
    trace_rbf = go.Scatter(
        x = dates,
        y = svr_rbf.predict(dates),
        name = 'RBF model',
        line = dict(
            color = ('rgb(205, 12, 24)'))
    )
    trace_lin = go.Scatter(
        x = dates,
        y = svr_lin.predict(dates),
        name = 'Linear model',
        line = dict(
            color = ('rgb(22, 96, 167)'))
    )
    trace_poly = go.Scatter(
        x = dates,
        y = svr_poly.predict(dates),
        name = 'Polynomial model',
        line = dict(
            color = ('rgb(189,189,189)'))
    )
    data = [values,trace_rbf,trace_lin,trace_poly]
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='basic-line')

    value = np.reshape([x],(-1, 1))
    return svr_rbf.predict(value)[0], svr_lin.predict(value)[0], svr_poly.predict(value)[0]

get_data('aapl.csv') # calling get_data method by passing the csv file to it

print ("Dates:", dates)
print ("Prices:", prices)
print (predict_price(dates, prices, 29))