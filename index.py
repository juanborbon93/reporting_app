import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from pony import orm
from app import app,server
from db import *
from pages import landing,community

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='main-page',style={'margin-bottom':'2em'})
])

@app.callback(
    Output('main-page','children'),
    [Input('url','pathname')]
)
def show_page(pathname):
    if pathname == None:
        return None
    if pathname == '/':
        return landing.layout()
    pathname = pathname.split('/')
    if  pathname[0:2] == ['','community'] and len(pathname)==3:
        return community.layout(pathname[-1])
    return html.H1('404 NOT FOUND')


if __name__ == '__main__':
    # app.server.run(host='0.0.0.0', port=5000,debug=True) 
    # app.run_server(host='0.0.0.0', port=5000)
    app.run_server()
    # serve(server,host='0.0.0.0', port=5000)