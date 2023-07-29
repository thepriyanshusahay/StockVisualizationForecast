import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

first_card = dbc.Card([
    dbc.CardBody([
        dbc.CardHeader(html.H5("Dash", className="card-title",style = {"textAlign":"center", 'fontFamily' : 'Comic Sans MS'}),),
        html.Br(),
        html.P("Dash is a python framework created by plotly for creating interactive web applications. Dash is written on the top of Flask, Plotly.js and React.js. With Dash, you don’t have to learn HTML, CSS and Javascript in order to create interactive dashboards, you only need python. Dash is open source and the application build using this framework are viewed on the web browser."),
        html.Br()
])
    
],color = "#E88B73",style ={'textAlign':'justified','color': "#FFFFF0",'fontFamily' : "lato"}
)
second_card = dbc.Card([
    dbc.CardBody([
        dbc.CardHeader(html.H5("yFinance", className="card-title",style = {"textAlign":"center", 'fontFamily' : 'Comic Sans MS'}),),
        html.Br(),
        html.P("Yfinance is a python package that enables us to fetch historical market data from Yahoo Finance API in a Pythonic way. We can easily download historical stock data from yfinance, but the problem is, it is very time taking. Hence, we use multithreading for covering up the time. Multithreading enables us to download large amounts of data by executing multiple threads concurrently.")
])
    
],color = "#E88B73",style ={'textAlign':'justified','color': "#FFFFF0",'fontFamily' : "lato"}
)
    
third_card = dbc.Card([
    dbc.CardBody([
        dbc.CardHeader(html.H5("Support Vector Machine", className="card-title",style = {"textAlign":"center", 'fontFamily' : 'Comic Sans MS'}),style ={'color' : '#FFFFF0'}),
        html.Br(),
        html.P("Support vector machines (SVMs) are a set of related supervised learning methods, popular for performing classification and regression analysis using data analysis and pattern recognition. Methods vary on the structure and attributes of the classifier. The goal is to maximize the margin between the hyperplane and the support vectors. Many consider SVM as the best off-the-shelf classifier.")
])
    
],color = "#E88B73",style ={'textAlign':'justified','color': "#FFFFF0",'fontFamily' : "lato"}
)     


info_card = dbc.Card([
     dbc.CardBody([
         dbc.CardHeader(html.H5("Go to Information", className="card-title",style = {"textAlign":"center", 'fontFamily' : 'Comic Sans MS'}),style ={'color' : '#FFFFF0'}),
         html.Br(),
        html.P("This project does a correct prediction of stocks that can lead to huge profits for the seller and the broker. It can be predicted by carefully analyzing the history of respective stock market. It predicts a market value close to the tangible value, thereby increasing the accuracy. We have used Machine Learning approach, which has dataset as vital part. In this project, supervised machine learning is employed on a dataset obtained from Yahoo Finance. Regression models are engaged for the conjecture separately. Finally, the graphs for the fluctuation of prices with the dates (in case of Regression based model) and between actual and predicted price (for the LSTM based model) are plotted."),
        html.Br()
        
])
],color = "#E88B73",style ={'textAlign':'justified','color': "#FFFFF0",'fontFamily' : "lato"})
requirement_card = dbc.Card([
    dbc.CardBody([
         dbc.CardHeader(html.H5("Things You Need to Know", className="card-title",style = {"textAlign":"center", 'fontFamily' : 'Comic Sans MS'}),style ={'color' : '#FFFFF0'}),
         html.Br(),
        html.P("The Processor required for the project is Pentium IV or above and it's speed should be 2.4 GHz. The capacity of Hard Disk and RAM must be at least 40 GB and 512 GB respectively. Microsoft Windows 7/8/8.1/10/Xp/Vista is the requirement for the Operating System and prgramming language used is Python, HTML and CSS. VS Code is required as an IDE Tool and CPython, JyPython or PyPy are some required interpreter. The project is based on the Dash Framework, and it can be run upon Chrome, Internet Explorer or Mozilla Explorer. Dash, Flask, Flask Compress, Gunicorn, LXML, Numpy, Pandas, Plotly, Scikit-Learn, Scipy, Sklearn, yfinance are some of the libraries used in this project.")
])
    
],color = "#E88B73",style ={'textAlign':'justified','color': "#FFFFF0",'fontFamily' : "lato"}
)

def layout():
    return html.Div([
        html.Br(),
        dbc.Row([
        dbc.Col([
    dcc.Markdown('# About', className='mt-3'),

        ], width={'size':6, 'offset':4}),
       
    html.Hr(),
], justify='center'),
       dbc.Row([
            dbc.Col(info_card, width = 6),
        dbc.Col(requirement_card, width = 6),
      ]),
      html.Br(),
      dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(second_card, width=4),
        dbc.Col(third_card, width =4),
        html.Br(),
        html.Br(),
        html.Hr()
        
    ]
      )
    ])
    