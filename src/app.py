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
    children=[
        # Do not change this div, if you wonder why it exists, do not hesiate to ask me (Pierre-Emmanuel)
        html.Div(
            id = 'state_holder',
            hidden = True,
            title = "nbVues",
            className = None,
            accessKey= "all"
        ),
        html.Header(
            children=[
                html.H1(
                    "L'utilisation de Tiktok par les médias francophones",
                    style={
                        "text-align": "left",
                        "margin-top": "1px",
                        "margin-bottom": "17px",
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
                        html.Div(
                            className="clock",
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
                                )
                            ],
                        ),
                    ],
                    style={
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "position": "relative",
                        "top": "30px",
                    },
                ),
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
                            children=[],
                        )
                    ]
                ),
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
                html.Div(
                    children=[
                        html.Div(
                            children=[],
                        )
                    ]
                ),
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
                                "width": "100px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                                "marginLeft": "700px",
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
                                "width": "100px",
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
                                "width": "100px",
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
    Output("state_holder", "title"),
    Output("state_holder", "className"),
    Output("state_holder", "accessKey"),
    Input("compte-btn", "n_clicks"),
    Input("tags-btn", "n_clicks"),
    Input("duree-btn", "n_clicks"),
    Input("vues-btn", "n_clicks"),
    Input("commentaires-btn", "n_clicks"),
    Input("likes-btn", "n_clicks"),
    Input("partages-btn", "n_clicks"),
    State('state_holder', 'title'),
    State('state_holder', 'className'),
    State('state_holder', 'accessKey'),
    prevent_initial_call = True
)
def update_output(c,t,d,v,co,l,p, metric, group_by_columns, year):
    if c == t == d == v == co == l == p == 0:
        return main_graph.get_empty_figure()
        
    if "compte-btn" == ctx.triggered_id:
        group_by_columns = 'compte'
    elif "tags-btn" == ctx.triggered_id:
        group_by_columns = 'tags'
    elif "duree-btn" == ctx.triggered_id:
        group_by_columns = 'durée'
    elif "vues-btn" == ctx.triggered_id:
        metric = 'nbVues'
    elif "commentaires-btn" == ctx.triggered_id:
        metric = 'nbCommentaires'
    elif "likes-btn" == ctx.triggered_id:
        metric = 'nbLikes'
    elif "partages-btn" == ctx.triggered_id:
        metric = 'nbPartages'
    
    fig = main_graph.get_figure(dataframe, group_by_columns, metric, year)
    return fig, metric, group_by_columns, year

@app.callback(
    Output("second_graph", "figure"),
    Input("main_graph", "clickData"),
    State('state_holder', 'className'),
    State('state_holder', 'accessKey'),
    prevent_initial_call = True
)
def update_output(click_data, group_by_columns, year):
    click_label = click_data['points'][0]['label']
    
    if group_by_columns == 'durée':
        return second_graph.get_figure(dataframe, [group_by_columns, click_label], year)
    
    click_current_path = click_data['points'][0]['currentPath']
    if click_current_path == '/':
        return second_graph.get_figure(dataframe, None, year)
    
    if click_label in ['France', 'Canada', 'Belgique', 'Suisse']:
        return second_graph.get_figure(dataframe, ['pays', click_label], year)

    return second_graph.get_figure(dataframe, [group_by_columns, click_label], year)
