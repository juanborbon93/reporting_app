import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from modules import form_v0
from db import *


def layout(community_name):
    try:
        community_name = community_name.replace('_',' ')
        community = Community(name=community_name)
        layout_output = [
            html.H1(f'{community.name} Incident Report Form'),
            html.P(community.greeting),
            html.A(
                html.H3(f'For your reference, you can find the {community} community guidelines here.'),
                src=community.guidelines,
                style={'display':'block'}
            )]
        layout_output = layout_output + form_v0.generate_form(community)
        return layout_output
    except:
        return html.H1('404 Not Found')