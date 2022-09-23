# coding: utf-8

# In[1]:

import importlib
import sys

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

# In[2]:

# sys.path.insert(0, 'C:\\Users\\Dikshit\\Documents\\WebsiteDir\\App\\Documents\\Unwanted')
# import YoutubeAnalyticsTest as YTA
# import Datatest as dt
# import Datasetmodule
#
# importlib.reload(Datasetmodule)
#
#
# def Youtube_Data(Data):
#     data1 = Data
#     print('This is calling Inside YOUTUBE TEST')
#     print(data1)
#
#     #data1 = Datasetmodule.csvdataset()
#     # nametest=Datasetmodule.csvname()
#
#     # In[4]:
#
#     # This will Give Channel Name,Total vidoes,Total Views and Subscribers
#
#     # CN=Datasetmodule.csvname()
#
#     # In[5]:
#
#     # Dash Components
#     # external_stylesheets = [dbc.themes.BOOTSTRAP]
#     # app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#     # app.title = 'Youtube Data'
#     external_stylesheets = [dbc.themes.BOOTSTRAP]
#     app=dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=False)
#     app.title = 'Youtube Data'
#
#     colors = {
#         'background': '#111111',
#         'bodyColor': '#F2DFCE',
#         'text': '#7FDBFF'
#     }
#
#     def get_page_heading_style():
#         return {'backgroundColor': colors['background']}
#
#     def get_page_heading_title():
#         return html.H1(children='YOUTUBE DATA',
#                        style={
#                            'textAlign': 'center',
#                            'color': colors['text']
#                        })
#
#     def get_page_heading_subtitle():
#         return html.Div(children='Insight of Youtube channels',
#                         style={
#                             'textAlign': 'center',
#                             'color': colors['text']
#                         })
#
#     def generate_page_header():
#         main_header = dbc.Row(
#             [
#                 dbc.Col(get_page_heading_title(), md=12)
#             ],
#             align="center",
#             style=get_page_heading_style()
#         )
#         subtitle_header = dbc.Row(
#             [
#                 dbc.Col(get_page_heading_subtitle(), md=12)
#             ],
#             align="center",
#             style=get_page_heading_style()
#         )
#         header = (main_header, subtitle_header)
#         return header
#
#     # # Generate Cards
#
#     def generate_card_content(card_header, card_value):
#         card_head_style = {'textAlign': 'center', 'fontSize': '150%'}
#         card_body_style = {'textAlign': 'center', 'fontSize': '200%'}
#         card_header = dbc.CardHeader(card_header, style=card_head_style)
#         card_body = dbc.CardBody(
#             [
#                 html.H5(f"{int(card_value):,}", className="card-title", style=card_body_style),
#             ]
#         )
#         card = [card_header, card_body]
#         return card
#
#     def generate_cards():
#         Total_videos = data1.shape[0]
#         Total_View = data1['View_count'].sum()
#         CN = ''
#         cards = html.Div(
#             [
#                 dbc.Row(
#                     [
#                         html.H2("Channel Name:" + CN, style={'textAlign': 'center', 'color': 'Red'}),
#                         html.Hr(),
#                         dbc.Col(dbc.Card(generate_card_content("Total View Count", Total_View), color="success",
#                                          inverse=True), md=dict(size=2, offset=3)),
#                         dbc.Col(dbc.Card(generate_card_content("Total Videos", Total_videos), color="warning",
#                                          inverse=True), md=dict(size=2)),
#                         dbc.Col(dbc.Card(generate_card_content("Total Subscribers", 0), color="dark", inverse=True),
#                                 md=dict(size=2)),
#                     ],
#                     className="mb-4",
#                 ),
#             ], id='card1'
#         )
#         return cards
#
#     # # Contents For Tab
#     tab1_content = dbc.Card(
#         dbc.CardBody(
#             [
#                 generate_cards(),
#             ]
#         ),
#     )
#
#     tab2_content = dbc.Card(
#         dbc.CardBody(
#             [
#                 YTA.teslayout(data1)
#             ]
#         ),
#     )
#
#     tab3_content = dbc.Card(
#         dbc.CardBody(
#             [
#                 html.Div(
#                     dbc.Row(
#                         [
#
#                             dbc.Label("1.Videos with Million Views will be highlighted in Green Color", color='Red'),
#                             dbc.Label("2.Any Column Fields can be Sorted(Ascending/Descending) using Arrorw Mark",
#                                       color='Red'),
#
#                             dbc.Col(
#
#                                 dt.table(data1)
#
#                             )
#                         ])
#                 )
#
#             ]
#         ),
#     )
#
#     app_tabs = html.Div([
#         dbc.Tabs([
#             dbc.Tab(label="Home", tab_id='Home_Tab'),
#             dbc.Tab(label="Trends", tab_id='Trend_Tab'),
#             dbc.Tab(label="DataTable", tab_id='DataTable_Tab'),
#         ],
#             id="tabs",
#             active_tab="Home_Tab"
#         ),
#     ], className="mt-3"
#     )
#
#     Home_layout = html.Div(
#         dbc.Row(
#             [
#                 dbc.Col(
#                     tab1_content
#                 )
#             ])
#     )
#
#     Trend_Layout = html.Div(
#
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dcc.Loading(children=tab2_content, type='graph', fullscreen=True)
#
#                 ),
#
#             ])
#     )
#
#     # DataTable Layout
#
#     Datatable_layout = html.Div(
#         dbc.Row(
#             [
#                 dbc.Col(
#                     tab3_content
#                 ),
#
#             ])
#     )
#
#     # # Generate App Layout
#
#     def generate_layout():
#         page_header = generate_page_header()
#
#         layout = dbc.Container(
#             [
#                 page_header[0],
#                 page_header[1],
#                 html.Hr(),
#                 dbc.Row(
#                     dbc.Col(app_tabs, width=12), className="mt-3"),
#                 html.Div(id='content', children=[]),
#                 html.Div(id='none', children=[], style={'display': 'none'}),
#                 html.Div(id='test', children=[], style={'display': 'none'})
#
#             ], fluid=True, style={'backgroundColor': colors['bodyColor']}
#         )
#         return layout
#
#     print('Im There before callback')
#
#     # @app.callback(
#     #     Output("content", "children"),
#     #     [Input("tabs", "active_tab")]
#     #
#     # )
#     # def switch_tab(tab_choosen):
#     #     print('I AM calling inside Callback')
#     #     if tab_choosen == 'Home_Tab':
#     #         return Home_layout
#     #     elif tab_choosen == 'Trend_Tab':
#     #         return Trend_Layout
#     #     elif tab_choosen == 'DataTable_Tab':
#     #         return Datatable_layout
#
#     layout1 = generate_layout()
#     return layout1
