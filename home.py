from ctypes import alignment
from turtle import width, window_width
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import base64

dash.register_page(__name__, path='/', order=0)
green_text = {'color':'green'}

# resume sample template from https://zety.com/
layout = html.Div([
    html.H1(),
    dcc.Markdown('# Vi-STOCKS', style={'textAlign':'center', 'fontFamily' : 'Impact'}),
    dcc.Markdown('Visualizing and Predicting Stocks', style={'textAlign': 'center'}),
    html.Br(),
   
    html.Br(),
    
    dbc.CardGroup(
    [
        dbc.Card([
            
            dbc.CardHeader( html.H5("VISUALIZE", className="card-title", style = {"textAlign":"center"}),
),           dbc.CardImg(src="/assets/viz1.jpg", top=True, bottom=False, alt='Learn Dash Bootstrap Card Component'),
            dbc.CardBody(
                [
                    html.P(
                        "Visualize the graphical representation of the stocks"
                        "In a fun and interactive way.",
                        className="card-text",
                    ),
                   
                    html.Br(), 
                    dbc.Button(
                        "Click here", color="success",  className="d-grid gap-2 col-6 mx-auto", href = "visualize"
                    ),
                ]
            )
    ]),
        dbc.Card([
            dbc.CardHeader(html.H5("PREDICT", className="card-title",style = {"textAlign":"center"})),
              dbc.CardImg(src="/assets/pre.jpg", top=True, bottom=False,
                     alt='Learn Dash Bootstrap Card Component'),
            dbc.CardBody(
                [
                    html.P(
                        "See the predicted values of stock price of future,"
                        "Using our prediction model."
                        ,
                        
                        className="card-text",
                    ),
                   
                    html.Br(),
                    dbc.Button(
                        "Click here", color="warning",  className="d-grid gap-2 col-6 mx-auto", href = "predict"
                    ),
                ]
            )
     ] ),
        dbc.Card([
            dbc.CardHeader(html.H5("ABOUT", className="card-title",style = {"textAlign":"center", 'fontFamily' : 'Comic Sans MS'}),),
              dbc.CardImg(src="/assets/au2.jpg", top=True, bottom=False,
                 alt='Learn Dash Bootstrap Card Component'),
            dbc.CardBody(
                [
                    html.P(
                        "Get to know about our web application's more technically. "
                          "By clicking the link below.",
                          
                        className="card-text",
                    ),
                     
                   
                    html.Br(),
                    dbc.Button(
                        "Click here", color="danger",  className="d-grid gap-2 col-6 mx-auto", href = "about"
                    ),
                ]
            )
     ] ),
    ]

),
    html.Br(),
    html.Br(),
  
    html.Br(),
    html.Br(),
   

    dcc.Markdown('###    CONTACT US', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
    dcc.Markdown('### Contacting Info', style={'color':'gray'}),
    dcc.Markdown('Address', style=green_text),
    dcc.Markdown('Greater Noida, India'),
    dcc.Markdown('Phone Number', style=green_text),
    dcc.Markdown('+91 938918xxxx'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('Vi_Stocks@gmail.com'),
        ], width={'size':6, 'offset':4})
], justify='center')
   ])
