import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
        [
            dcc.Graph(id='live_graph',animate=True),
            #to trigger an event for us every 1000ms
            dcc.Interval(
                id='graph_update',
                interval=1000
                ) 
            ]
        )

@app.callback(Output('live_graph','figure'),
        events = [Event('graph_update','interval')])
def update_graph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(random.randint(1,20))

    data = go.Scatter(
            x = list(X),
            y = list(Y),
            name='Scatter PLot',
            mode = 'lines+markers'
            )
    
    return {'data':[data], 'layout': go.Layout(xaxis = dict(range=[min(X),max(X)]),yaxis = dict(range=[min(Y),max(Y)]) ) }

if __name__ == '__main__':
    app.run_server()

    







