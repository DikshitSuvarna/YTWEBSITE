# coding: utf-8

# In[13]:
import importlib

import dash
from dash import callback
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
from dash import dash_table
from IPython.display import HTML
import dash_bootstrap_components as dbc
import time
import sys
import os

#sys.path.insert (0, 'C:\\Users\\Dikshit\\Documents\\WebsiteDir\\App\\Documents\\Unwanted')
sys.path.insert(0,'C:\\Users\\Dikshit\\Documents\\WebsiteDirectory\\App\\Documents\\Packages')
import Yotube_Module as YT
import Datasetmodule

importlib.reload (Datasetmodule)

# In[15]:


import pandas as pd

# os.chdir('D:\\Complete DataScience\\WebsiteDir')
# from Apptest import app

newpath = "Documents\\YTDT"
if not os.path.exists (newpath):
    os.makedirs (newpath)
os.chdir ('Documents\\YTDT')

dash.register_page (__name__, path='/')

layout = html.Div (
    [
        html.H5 ("Here We Go....!!!",
                 style={"display": "flex", "justifyContent": "center", "color":"blue"}),
        dbc.InputGroup (
            [
                dbc.Input (
                    id="ticker-search3",
                    placeholder="Enter Channel ID",
                    style={"maxWidth": 400},
                ),
            ],
            style={"display": "flex", "justifyContent": "center",
                   "padding": "10px", "border-radius": "10px", "width": "100%"},
        ),
        html.Br (),
        html.Div ([
            dcc.Link (
                dbc.Button (children="submit", n_clicks=0, id="ticker-search2-btn"),
                id="ticker-search2-link",
                href="/",
            ),
        ],
            style={"display": "flex", "justifyContent": "center"},
        ),
        dbc.Row (
            dbc.Col (
                dcc.Loading (children=[
                    dbc.Col (id='table', style={"display": "flex", "justifyContent": "center","padding": "10px","color":"Red"})],
                    color='#119DFF',
                    type="dot", fullscreen=True)

            )
        ),
        html.P (
            [
                html.Span (
                    "How to get Channel ID",
                    id="tooltip-target",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                ),
            ],
            style={"display": "flex", "justifyContent": "center", "padding": "10px"},
        ),
            dbc.Tooltip (
            "Go Youtube channel Which You want to see Data..."
            "Right click=>View Page Source..."
            "Press CTRL+F and type channelid click on '˅' symbol..."
            "Copy the content of Channel ID",
            target="tooltip-target",
            placement= 'right'
        ),
        html.A ("Didn't Get Watch here...", href="https://www.youtube.com/watch?v=D12v4rTtiYM", target="_blank",
                style={"display": "flex", "justifyContent": "center"})

    ]
)


@callback (
    Output ("ticker-search2-link", "href"),
    Output ("table", component_property='children'),
    Output ("ticker-search2-btn", component_property='children'),
    Output ("store-data", component_property='data'),
    [Input ("ticker-search2-btn", "n_clicks")],
    [State ('ticker-search3', component_property='value')],
    prevent_initial_call=True
)
def search (n_clicks, ticker):
    if ticker is None or ticker == "":

        return "", "Please Enter Channel ID", dash.no_update, ""
    else:
        try:
            #dataframe=YT.getinfo(ticker)
            #print(dataframe)
            #subscount = YT.subscribercount (ticker)
            value = 'Success'
            #dataframe1 = Datasetmodule.csvdataset ()
            store = {
                #"data": dataframe1.to_dict ("records"),
                "name": Datasetmodule.csvname (),
                #"subscount": subscount
                "subscount": 0,
            }
        except:

            return "", "Something Went Wrong", dash.no_update, ""

    return '/pages/hometestpage', value, "Click on to See...Results", store
