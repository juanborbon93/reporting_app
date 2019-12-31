import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from db import *

name = dbc.FormGroup(
    [
        dbc.Label("Your Name:", html_for="name"),
        dbc.Input(type="Text", id="name", placeholder="Enter Name"),
        dbc.FormText(
            "Enter your full name (optional)",
            color="secondary",
        ),
    ]
)

email = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="email"),
        dbc.Input(type="email", id="email", placeholder="Enter email address"),
        dbc.FormText(
            "Fill this if you would like us to get in contact with you",
            color="secondary",
        ),
    ]
)


issue_type = dbc.FormGroup(
    [
        dbc.Label("Type of issue you are reporting:",html_for="issue-type-input"),
        dbc.RadioItems(
            options=[
                {"label": "Community Member Misconduct", "value": 'Community Member Misconduct'},
                {"label": "Opportunity for community/culture improvement", "value": 'Opportunity for community/culture improvement'},
                {"label": "Other", "value": 'Other'}
            ],
            value=1,
            id="issue-type-input",
        ),
        dbc.Label('Please Explain:'),
        dbc.Input(type='text',id='other-issue-explanation')
    ]
)


details = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Textarea(
            bs_size='md',
            placeholder='Please describe the details of your issue. '
        ),
        dbc.FormText(
            "Are you on email? You simply have to be these days",
            color="secondary",
        ),
    ]
)


additional_contacts = dbc.FormGroup(
    [
        dbc.Label("Names of people who can provide additional information ", html_for="additional-contacts"),
        dbc.Input(type="text", id="additional-contacts", placeholder="Enter names"),
    ]
)


name_disclosure_consent = dbc.FormGroup(
    [
        dbc.Label("If you provided your name above, do you consent to community advocates disclosing your name to the other person/people involved in this issue? ", html_for="disclosure-consent"),
        dbc.RadioItems(
            options=[
                {"label": "Yes", "value": 'yes'},
                {"label": "No", "value": 'no'},
            ],
            id="disclosure-consent",
        ),
    ]
)

ideal_resolution = dbc.FormGroup(
    [
        dbc.Label("What does an ideal resolution to this issue look like to you? ", html_for="ideal-resolution"),
        dbc.Textarea(
            invalid=True, bs_size="lg", placeholder="Describe here",id='ideal-resolution'
        ),
    ]
)

def generate_form(community_info):
    output = [
        name,
        email,
        issue_type,
        details,
        additional_contacts,
        name_disclosure_consent,
        ideal_resolution
    ]

    return output