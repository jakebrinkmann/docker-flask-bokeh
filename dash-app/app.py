# Example base: https://plot.ly/dash/getting-started-part-2
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

data = {2017: range(0, 100),
        2016: range(100, 200),
	2015: range(0, 10, 2)}

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider', animate=True),
    dcc.Slider(
        id='year-slider',
        min=2015,
        max=2017,
        value=2017,
        step=1,
        marks={str(i):str(i) for i in data.keys()}
    )
])

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = data[selected_year]
    traces = []
    for m in range(0,10,3):
        traces.append(go.Scatter(
            y=map(lambda x: x * m, filtered_df),
            x=range(0,100),
            text='m={}'.format(m),
            mode='markers',
            opacity=0.7,
            marker={
        	'size': 15,
        	'line': {'width': 0.5, 'color': 'white'}
            },
            name='{}x'.format(m)
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'linear', 'title': 'Sweet inputs, yo'},
            yaxis={'title': 'Going UP', 'range': [0, 1000]},
            margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')

