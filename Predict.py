import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from .side_bar import sidebar
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf

dash.register_page(__name__, title='App1', order=1)

df = pd.read_csv('https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')
search = {}

df = pd.read_csv(
    'https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')

df = pd.read_csv('https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')
ac = df['Company Name'].tolist()
key = df['Symbol'].tolist()
for i in range(len(ac)):
    search[ac[i]] = key[i]

first_card = dbc.Card(
            dbc.CardBody([
                  html.Br(),
            
            html.Br(),
            html.H5("To know about the company and it's stocks price enter the ticker..",style ={'textAlign':'center','fontFamily' : "lato"}),
            html.Br(),
            html.Br(),
            html.H5("ENTER TICKER", className="card-title"),
            dbc.Input(id ="ticker_id", placeholder="Type here....", type="text", className= "mb-3",value ="AAPL"),
            html.Br(),
            html.H5("ENTER NO. OF DAYS", className="card-title"),
            dbc.Input(id ="days_id" ,placeholder="Type here....", type="text", className= "mb-3",value ="10"),
            html.Br(),
            html.Div([dbc.Button("Get Graph", color="dark",
                     className="d-grid gap-2 col-6 mx-auto", id="my-butt", n_clicks=0),
                      dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Wrong Entry")),
                dbc.ModalBody("The ticker you entered is either not valid or currently not available. For help check the list with Help."),
            ],
            id="mod-sm",
            size="sm",
            is_open=False,
            centered = True,
            scrollable = True,
        )]),
            html.Br(),
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

              ])
              
              ,color = "warning",style ={'textAlign':'center','color': "#111211",'fontFamily' : "lato"},
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.Br(),
            html.H5("Predicted Closing Stock Price", className="card-title"),
            html.Br(),
            dcc.Graph(id="pre_graph_id",figure={})
           
        ]
    )
)

def layout():
    return html.Div([
        html.Br(),
        dbc.Row([
        dbc.Col([
    dcc.Markdown('# Predict', className='mt-3'),

        ], width={'size':6, 'offset':4}),
       
    html.Hr(),
], justify='center'),
        dbc.Row(
        [
            
            dbc.Col(first_card, width = 4 
    ),
            dbc.Col(second_card,width = 8)
])
    ])

@callback(
      Output("pre_graph_id","figure"),
      [Input(component_id="my-butt", component_property= "n_clicks")],
      [State(component_id="ticker_id",component_property= "value"),
      State(component_id="days_id",component_property= "value")],
      prevent_initial_call = False,
  )

def update_graph(n,value,days):
    tick = str(value)
    print(type(days))
    day = int(days)
    df = yf.Ticker(tick)
    df = df.history(period="max")
    df = df[['Close']]
    forecast_out = day
    df['Prediction'] = df[['Close']].shift(-forecast_out)
    X = np.array(df.drop(['Prediction'],1))
    X = X[:-forecast_out]
    Y = np.array(df['Prediction'])
    Y = Y[:-forecast_out]
    x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2)
    svr_rbf = SVR(kernel = 'rbf', C=1e3,gamma = 0.1)
    svr_rbf.fit(x_train,y_train)
    svm_confidence = svr_rbf.score(x_test,y_test)
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    lr_confidence = lr.score(x_test,y_test)
    x_forecast = np.array(df.drop(['Prediction'],1))[-forecast_out:]
    svm_prediction = svr_rbf.predict(x_forecast)
    print(svm_prediction)
    date =dt.datetime.now()
    date1 =date.strftime("%x")
    times = pd.date_range(date1, periods=forecast_out, freq='B')
    dff = pd.DataFrame(list(zip(times,svm_prediction)),
               columns =['Date', 'Prediction'])
    fig = px.area(dff, x='Date', y="Prediction")

    return fig

@callback(
    Output("mod-sm", "is_open"),
    Input("my-butt", "n_clicks"),
    [State("mod-sm", "is_open"),State("ticker_id", "value")]
)

def toggle_modal(n1, is_open, value):
    df = pd.read_csv('https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv')
    ac = df['Symbol'].tolist()
    val = str(value)
    if n1 and val.upper() not in ac:
        return not is_open
    return is_open
