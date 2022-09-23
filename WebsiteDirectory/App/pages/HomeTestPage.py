

import importlib

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input
from dash import  callback

import dash_bootstrap_components as dbc
import dash_extensions as de

import sys

#sys.path.insert(0,'C:\\Users\\Dikshit\\Documents\\WebsiteDir\\App\\Documents\\Unwanted')
sys.path.insert(0,'C:\\Users\\Dikshit\\Documents\\WebsiteDirectory\\App\\Documents\\Packages')
import YoutubeTest as yt
import Datasetmodule
import Datatest as dt
importlib.reload(Datasetmodule)
import YoutubeTest as yt
import Tabs as tb



url='https://assets4.lottiefiles.com/packages/lf20_3fuksula.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


dash.register_page(__name__,)


layout=html.Div([
            html.Div(de.Lottie(options=options, width="50%", height="50%", url=url),id='Loitte',hidden=False),
            #html.H3('Loading Components...',id='LoadComp',hidden=False),
            dcc.Loading(children=[dbc.Row(id='testforlayout')],color='#119DFF',type="graph",fullscreen=True)


])



@callback(
         Output("content1", "children"),
         [Input("tabs", "active_tab")],
)
def switch_tab (tab_choosen):
    print('callback test')
    if tab_choosen == 'Home_Tab':
        return tb.Home_layout()
    elif tab_choosen == 'Trend_Tab':
        return tb.Trend_layout()
    elif tab_choosen == 'DataTable_Tab':
        return tb.Datatable_layout()



@dash.callback(
    Output("Loitte","hidden"),
    Output("testforlayout", "children"),
    Input("store-data",component_property='data'),
    #prevent_initial_call=True
)
#
def update(data):
     name=data.get('name')
     #some=data.get("data")
     data1=Datasetmodule.csvdataset()
     subcount=data.get("subscount")
     #data1=pd.DataFrame(some)
     return True,tb.functionoflayout(data1,subcount)




