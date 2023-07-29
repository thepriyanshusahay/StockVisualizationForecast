from turtle import color
import plotly.express as px
import yfinance as yf
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import datetime as dt
from dash import dash_table
import pandas as pd
from dash import Input, Output, callback, State

dash.register_page(__name__, order=2)

search = {}

df = pd.read_csv(
    'https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')

df = pd.read_csv('https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')
ac = df['Company Name'].tolist()
key = df['Symbol'].tolist()
for i in range(len(ac)):
    search[ac[i]] = key[i]

    

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.Br(),
            html.Br(),
            html.H5("ENTER TICKER", className="card-title"),
            html.P("To know about the company and it's stocks price enter the ticker", style={
                   'textAlign': 'center','fontFamily': "lato"}),
            dbc.Input(id="ticker_id", placeholder="Type here....",
                      type="text", className="mb-3", value=""),
            html.Br(),


            html.Div([dbc.Button("Get Info", color="dark",
                     className="d-grid gap-2 col-6 mx-auto", id="my-button", n_clicks=0),
                      dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Wrong Entry")),
                dbc.ModalBody("The ticker you entered is either not valid or currently not available. For help check the list with Help."),
            ],
            id="modal-sm",
            size="sm",
            is_open=False,
            centered = True,
            scrollable = True,
        )]),


            html.Br(),
            html.P("Forget the ticker? Check the ticker list",
                   style={'textAlign': 'center'}),
            html.Div(
                [
                    dbc.Button("Help", color="dark",
                               className="d-grid gap-2 col-6 mx-auto", id="open-offcanvas", n_clicks=0),
                    dbc.Offcanvas(
                        
                        dbc.Container([
                            
                            dcc.Dropdown(ac, ac[0], id='demo-dropdown'),
                            html.Div(id='dd-output-container'),
                            html.Br(),
                            dash_table.DataTable(
                                df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns],
                                style_header={'border': '1px solid black'},
                                style_cell={
                                    'border': '1px solid grey', 'textAlign': 'left', 'color': 'black', 'fontFamily': 'Lato'}
                            ),
                        ]),
                        id="offcanvas",
                        title="Ticker List",
                        is_open=False,
                        scrollable=True,


                ),
                ]
            )


        ]
    ), color="success", style={'textAlign': 'center', 'color': "#FFFFF0", 'fontFamily': "lato"},
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Company Information", className="card-title"),
            html.H1(id="output2", className="card-title", children=""),
            html.Div(id="output", children=""),


        ]
    )
)
third_card = dbc.Card(
    dbc.CardBody(
        [
            html.Br(),
            html.H5("Opening and Closing Stock Price", className="card-title"),
            html.Br(),
            dcc.RadioItems(
                id = "options1",
   options=[
       {'label': ' 5 Day    ,', 'value': '5d'},
       {'label': ' 1 Month    ,', 'value': '1mo'},
       {'label': ' 3 Month    ,', 'value': '3mo'},
       {'label': ' 6 Month    ,', 'value': '6mo'},
       {'label': ' 1 Year    ,', 'value': '1y'},
       {'label': ' 2 Year    ,', 'value': '2y'},
       {'label': ' 5 Year    ,', 'value': '5y'},
       {'label': ' All Time    ', 'value': 'max'},
   ],
   value='1y',
   style = {"width" : '200%'}
),
 html.Br(),
            dcc.RadioItems(
                id = "options2",
   options=[
       {'label': ' Area Chart    ,', 'value': 'area'},
       {'label': ' Line Chart   ', 'value': 'line'},
       
   ],
   value='area',
   style = {"width" : '200%'}
),
            dcc.Graph(id="graph_id")

        ]
    )
)


def layout():
    return html.Div([
        html.Br(),
        dbc.Row([
        dbc.Col([
    dcc.Markdown('# Visualize', className='mt-3'),

        ], width={'size':6, 'offset':4}),
       
    html.Hr(),
], justify='center'),
        dbc.Row(
            [
                dbc.Col(first_card, width=4),
                dbc.Col(second_card, width=8),

            ]
        ),
        html.Br(),
        dbc.Row([
            dbc.Col(third_card, width=12)

        ])

    ])


@callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(
    [Output(component_id="output", component_property="children"),
     Output(component_id="output2", component_property="children"),
     Output(component_id="graph_id", component_property="figure")],
    [Input(component_id="my-button", component_property="n_clicks"),
     Input("options1", "value"),  Input("options2","value")],
    [State(component_id="ticker_id", component_property="value")],
    prevent_initial_call=False,

)
def output_text(n, time, type, value):
    df = pd.read_csv('https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')
    ac = df['Symbol'].tolist()
    val = str(value)
    if len(value) == 0 or val.upper() not in ac:
        return dash.no_update
    else:
        tick = str(value)
        ti = yf.Ticker(tick)
        inf = ti.info
        df = ti.history(period=time)
        dff = df[['Close']]
        dff['Date'] = df.index
        dff['Open'] = df[['Open']]
        if type == 'area':
            fig = px.area(dff, x='Date', y=dff.columns)
        else:
            fig = px.line(dff, x='Date', y=dff.columns)

        return inf['longBusinessSummary'], inf['shortName'], fig


@callback(
    Output("modal-sm", "is_open"),
    Input("my-button", "n_clicks"),
    [State("modal-sm", "is_open"),State("ticker_id", "value")]
)

def toggle_modal(n1, is_open, value):
    df = pd.read_csv('https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')
    ac = df['Symbol'].tolist()
    val = str(value)
    if n1 and val.upper() not in ac:
        return not is_open
    return is_open

@callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if len(value) == 0:
        return dash.no_update
    return f'Ticker of selected company is {search[value]}'    