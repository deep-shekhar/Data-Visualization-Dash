import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas_datareader.data as web
import datetime

stock = 'HPE'

#df.reset_index(inplace=True) 
#print(df.head())

app = dash.Dash()
app.layout = html.Div(children=[
    html.Div(children='''Stock symbol to graph'''),
    
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
    
    ])

@app.callback(
        Output(component_id='output-graph', component_property='children'),
        [Input(component_id='input', component_property='value')])
def update_graph(input_data):
    try:
        start = datetime.datetime(2015, 1, 1)
        end = datetime.datetime.now()
        df = web.DataReader(input_data,"yahoo", start, end) 
        return dcc.Graph(
                id='exapmle-graph',
                figure={
                    'data': [
                        {'x':df.index, 'y':df.Close,'type':'line','name':input_data}
                        ],
                    'layout':{'title':input_data}
                    }
                )
    except:
        return "ERROR!"

if __name__ == '__main__':
    app.run_server()