# -*- coding: utf-8 -*-

"""
    File name: app.py
    Projet TikTok
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import ctx
import plotly.express as px

import pandas as pd

import preprocess
import main_graph
import clock
import template
import second_graph


app = dash.Dash(__name__)
app.title = "PROJET | INF8808"

dataframe = pd.read_csv("./assets/data/tiktokMediasFranco.csv")
preprocess.preprocess_initial(dataframe)
data_pie = preprocess.pie_chart(dataframe)

template.create_custom_theme()
template.set_default_theme()

app.layout = html.Div(
    className="content",
        style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'right': 0,
        'bottom': 0,
        'aspect-ratio': '16 / 9',
    },
    children=[
        # Do not change this div, if you wonder why it exists, do not hesitate to ask me (Pierre-Emmanuel)
        html.Div(
            id = 'state_holder',
            hidden = True,
            children=[
                html.Div(
                    id='metric_state',
                    key = 'nbVues'
                ),
                html.Div(
                    id='year_state',
                    key = '2019-2022'
                ),
                html.Div(
                    id='group_state',
                    key = None
                ),
                html.Div(
                    id='selected_state_1',
                    key = None
                ),
                html.Div(
                    id='selected_state_2',
                    key = None
                )
            ]
        ),
        html.Header(
            children=[
                html.H1(
                    "L'utilisation de Tiktok par les médias francophones",
                    style={
                        'position':'fixed',
                        'top':'20px',
                        'left':'20px',
                        "font-family": "Perpetua Titling MT Bold",
                        "font-size": "45px",
                    },
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.H2(
                                            children="Le sujet le plus discuté ce mois",
                                            style={
                                                "color": "white",
                                                "text-align": "center",
                                                "font-size": "18px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "background-color": "rgb(22 78 99)",
                                        "padding": "10px",
                                        "width": "50%",
                                    },
                                ),
                                html.Div(
                                    children=[
                                        html.H2(
                                            children="#Coronavirus",
                                            style={
                                                "color": "black",
                                                "text-align": "center",
                                                "font-size": "25px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "background-color": "white",
                                        "padding": "10px",
                                        "width": "50%",
                                    },
                                ),
                            ],
                            style={
                                "display": "inline-flex",
                                "flex-direction": "row",
                                "margin-bottom": "20px",
                                "margin-right": "20px",
                                "border": "2px solid black",
                                "height": "20%",
                                "width": "23%",
                            },
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.H2(
                                            children="Le média à l'affiche ce mois",
                                            style={
                                                "color": "white",
                                                "text-align": "center",
                                                "font-size": "18px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "background-color": "rgb(22 78 99)",
                                        "padding": "10px",
                                        "width": "50%",
                                    },
                                ),
                                html.Div(
                                    children=[
                                        html.H2(
                                            children="HUGODECRYPTE",
                                            style={
                                                "color": "black",
                                                "text-align": "center",
                                                "font-size": "25px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "background-color": "white",
                                        "padding": "10px",
                                        "width": "50%",
                                    },
                                ),
                            ],
                            style={
                                "display": "inline-flex",
                                "flex-direction": "row",
                                "margin-bottom": "20px",
                                "margin-right": "20px",
                                "border": "2px solid black",
                                "height": "20%",
                                "width": "27%",
                            },
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.H2(
                                            children="Nombre de Tik Tok publiés ce mois",
                                            style={
                                                "color": "white",
                                                "text-align": "center",
                                                "font-size": "18px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "background-color": "rgb(22 78 99)",
                                        "padding": "10px",
                                        "width": "50%",
                                    },
                                ),
                                html.Div(
                                    children=[
                                        html.H2(
                                            children="324",
                                            style={
                                                "color": "black",
                                                "text-align": "center",
                                                "font-size": "25px",
                                            },
                                        ),
                                    ],
                                    style={
                                        "background-color": "white",
                                        "padding": "10px",
                                        "width": "50%",
                                    },
                                ),
                            ],
                            style={
                                "display": "inline-flex",
                                "flex-direction": "row",
                                "margin-bottom": "20px",
                                "border": "2px solid black",
                                "height": "20%",
                                "width": "25%",
                            },
                        ),
                     
                    ],
                    style={
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "left",
                        "position": "relative",
                        "top": "20px",
                        "margin-top": "80px",
                    },
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="clock",
                            className="graph",
                            figure=clock.get_clock(data_pie),
                            config=dict(
                                scrollZoom=False,
                                showTips=False,
                                showAxisDragHandles=False,
                                doubleClick=False,
                                displayModeBar=False,
                            ),
                        ),
                    ],
                   style={
                        'position': 'fixed',
                        'right': '30px',
                        'bottom': '82%',
                        'width': '275px',
                        'height': '275px',
                        'padding': '0px',
                        'margin': '0px',
                        'border': 'none',
                        'aspect-ratio':'16/9'
                    }
                )
            ]
        ),
        html.Main(
            className="viz-container",
            children=[
                html.Div(
                    children=[
                        html.Button(
                            "Vues",
                            id="vues-btn",
                            style={
                                "font-size": "11px",
                                "backgroundColor": "rgb(22 78 99)",
                                "color": "white",
                                'fontWeight': 'bold',
                                "width": "140px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                            },
                            n_clicks = 0
                        ),
                        html.Button(
                            "Likes",
                            id="likes-btn",
                            style={
                                "font-size": "11px",
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "140px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                            },
                            n_clicks = 0
                        ),
                        html.Button(
                            "Commentaires",
                            id="commentaires-btn",
                            style={
                                "font-size": "11px",
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "140px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                            },
                            n_clicks = 0
                        ),
                        html.Button(
                            "Partages",
                            id="partages-btn",
                            style={
                                "font-size": "11px",
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "140px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                            },
                            n_clicks = 0
                        ),
                    ],
                    style={"width": "150px"},
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
    
                                dcc.Graph(
                                    id="main_graph",
                                    className="graph",
                                    # figure=main_chart.get_figure(dataframe, group_by_columns, metric, year),
                                    figure=main_graph.get_empty_figure(),
                                    config=dict(
                                        scrollZoom=False,
                                        showTips=False,
                                        showAxisDragHandles=False,
                                        doubleClick=False,
                                        displayModeBar=False,
                                    ),
                                ),

                            ],
                        )
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                    
                                dcc.Graph(
                                    id="second_graph",
                                    className="graph",
                                    # figure=main_chart.get_figure(dataframe, group_by_columns, metric, year),
                                    figure=second_graph.get_figure(dataframe, None, "all"),
                                    config=dict(
                                        scrollZoom=False,
                                        showTips=False,
                                        showAxisDragHandles=False,
                                        doubleClick=False,
                                        displayModeBar=False,
                                    )
                                ),
                            ],
                        )
                    ]
                ),
            ],
        ),
        html.Div(
            dcc.RangeSlider(2019, 2022,
                id = 'year_slider',
                step=1,
                value=[2019, 2022],
                marks = {
                    2019:2019,
                    2020:2020,
                    2021:2021,
                    2022:2022
                },
            ),style={
                'position': 'absolute',
                'left': '12%',
                'right': '44%',
                'top':'85%'
            }
        ),
        
        html.Footer(
            children=[
                html.Div(
                    [
                        html.Button(
                            "Médias",
                            id="compte-btn",
                            style={
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "120px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                                "marginLeft": "410px",
                                "marginBottom": "60px",
                            },
                            n_clicks = 0
                        ),
                        html.Button(
                            "Sujets",
                            id="tags-btn",
                            style={
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "120px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                                "marginLeft": "20px",
                                "marginBottom": "60px",
                            },
                            n_clicks = 0
                        ),
                        html.Button(
                            "Durées",
                            id="duree-btn",
                            style={
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "120px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                                "marginLeft": "20px",
                                "marginBottom": "60px",
                            },
                            n_clicks=0
                        ),
                    ]
                ),
            ]
        ),
    ],
)


@app.callback(
    Output("main_graph", "figure"),
    Output("metric_state", "key"),
    Output("group_state", "key"),
    Output("year_state", "key"),
    Output("compte-btn", "style"),
    Output("tags-btn", "style"),
    Output("duree-btn", "style"),
    Output("vues-btn", "style"),
    Output("commentaires-btn", "style"),
    Output("likes-btn", "style"),
    Output("partages-btn", "style"),   
    Input("compte-btn", "n_clicks"),
    Input("tags-btn", "n_clicks"),
    Input("duree-btn", "n_clicks"),
    Input("vues-btn", "n_clicks"),
    Input("commentaires-btn", "n_clicks"),
    Input("likes-btn", "n_clicks"),
    Input("partages-btn", "n_clicks"),    
    Input("year_slider", "value"),
    State('metric_state', 'key'),
    State('group_state', 'key'),
    State('year_state', 'key'),
    State("compte-btn", "style"),
    State("tags-btn", "style"),
    State("duree-btn", "style"),
    State("vues-btn", "style"),
    State("commentaires-btn", "style"),
    State("likes-btn", "style"),
    State("partages-btn", "style"),   
    prevent_initial_call = True
)
def update_main_graph(c,t,d,v,co,l,p,year_value, metric, group_by_columns, year, compte_style, tags_style, duree_style, vues_style, comm_style, likes_style, partages_style):
    if "compte-btn" == ctx.triggered_id:
        group_by_columns = 'compte'
        compte_style['backgroundColor'] = "rgb(22 78 99)"
        tags_style['backgroundColor'] = 'white'
        duree_style['backgroundColor'] = 'white'
        
        compte_style['color'] = 'white'
        tags_style['color'] = 'black'
        duree_style['color'] = 'black'
        
        compte_style['fontWeight'] = 'bold'
        tags_style['fontWeight'] = ''
        duree_style['fontWeight'] = ''
    elif "tags-btn" == ctx.triggered_id:
        group_by_columns = 'tags'
        compte_style['backgroundColor'] = 'white'
        tags_style['backgroundColor'] = "rgb(22 78 99)"
        duree_style['backgroundColor'] = 'white'
        
        compte_style['color'] = 'black'
        tags_style['color'] = 'white'
        duree_style['color'] = 'black'
        
        compte_style['fontWeight'] = ''
        tags_style['fontWeight'] = 'bold'
        duree_style['fontWeight'] = ''
        
    elif "duree-btn" == ctx.triggered_id:
        group_by_columns = 'durée'
        compte_style['backgroundColor'] = 'white'
        tags_style['backgroundColor'] = 'white'
        duree_style['backgroundColor'] = "rgb(22 78 99)"
        
        compte_style['color'] = 'black'
        tags_style['color'] = 'black'
        duree_style['color'] = 'white'
        
        compte_style['fontWeight'] = ''
        tags_style['fontWeight'] = ''
        duree_style['fontWeight'] = 'bold'
        
    elif "vues-btn" == ctx.triggered_id:
        metric = 'nbVues'
        vues_style['backgroundColor'] = "rgb(22 78 99)"
        comm_style['backgroundColor'] = 'white'
        likes_style['backgroundColor'] = 'white'
        partages_style['backgroundColor'] = 'white'
        
        vues_style['color'] = "white"
        comm_style['color'] = 'black'
        likes_style['color'] = 'black'
        partages_style['color'] = 'black'
        
        vues_style['fontWeight'] = "bold"
        comm_style['fontWeight'] = ''
        likes_style['fontWeight'] = ''
        partages_style['fontWeight'] = ''
    elif "commentaires-btn" == ctx.triggered_id:
        metric = 'nbCommentaires'
        vues_style['backgroundColor'] = 'white'
        comm_style['backgroundColor'] = "rgb(22 78 99)"
        likes_style['backgroundColor'] = 'white'
        partages_style['backgroundColor'] = 'white'
        
        vues_style['color'] = "black"
        comm_style['color'] = 'white'
        likes_style['color'] = 'black'
        partages_style['color'] = 'black'
        
        vues_style['fontWeight'] = ""
        comm_style['fontWeight'] = 'bold'
        likes_style['fontWeight'] = ''
        partages_style['fontWeight'] = ''
    elif "likes-btn" == ctx.triggered_id:
        metric = 'nbLikes'
        vues_style['backgroundColor'] = 'white'
        comm_style['backgroundColor'] = 'white'
        likes_style['backgroundColor'] = "rgb(22 78 99)"
        partages_style['backgroundColor'] = 'white'
        
        vues_style['color'] = "black"
        comm_style['color'] = 'black'
        likes_style['color'] = 'white'
        partages_style['color'] = 'black'
        
        vues_style['fontWeight'] = ""
        comm_style['fontWeight'] = ''
        likes_style['fontWeight'] = 'bold'
        partages_style['fontWeight'] = ''
    elif "partages-btn" == ctx.triggered_id:
        metric = 'nbPartages'
        vues_style['backgroundColor'] = 'white'
        comm_style['backgroundColor'] = 'white'
        likes_style['backgroundColor'] = 'white'
        partages_style['backgroundColor'] = "rgb(22 78 99)"
        
        vues_style['color'] = "black"
        comm_style['color'] = 'black'
        likes_style['color'] = 'black'
        partages_style['color'] = 'white'
        
        vues_style['fontWeight'] = ""
        comm_style['fontWeight'] = ''
        likes_style['fontWeight'] = ''
        partages_style['fontWeight'] = 'bold'
    elif "year_slider" == ctx.triggered_id:
        year = str(year_value[0]) + "-" +str(year_value[1])

    fig = main_graph.get_figure(dataframe, group_by_columns, metric, year)
    return fig, metric, group_by_columns, year, compte_style, tags_style, duree_style, vues_style, comm_style, likes_style, partages_style

@app.callback(
    Output("second_graph", "figure"),
    Input("main_graph", "clickData"),
    Input('year_state', 'key'),
    State('group_state', 'key'),
    prevent_initial_call = True
)
def update_second_graph(click_data, year, group_by_columns):
    # If the callback is triggered by a click to the main graph
    if click_data is not None : 
        click_label = click_data['points'][0]['label']
        
        if group_by_columns == 'durée':
            return second_graph.get_figure(dataframe, [group_by_columns, click_label], year)
        
        click_current_path = click_data['points'][0]['currentPath']
        if click_current_path == '/':
            return second_graph.get_figure(dataframe, None, year)
        
        if click_label in ['France', 'Canada', 'Belgique', 'Suisse']:
            return second_graph.get_figure(dataframe, ['pays', click_label], year)

        return second_graph.get_figure(dataframe, [group_by_columns, click_label], year)

    # If the callback is triggered by a change of dates
    return second_graph.get_figure(dataframe, None, year)