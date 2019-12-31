import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

def layout():
    return html.H1('Hello')

test_output = [
    html.H1('This is the landing page')
]