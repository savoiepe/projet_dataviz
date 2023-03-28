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
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pandas as pd

import preprocess
import heatmap
import line_chart
import template


app = dash.Dash(__name__)
app.title = "PROJET | INF8808"

dataframe = pd.read_csv("./assets/data/tiktokMediasFranco.csv")
preprocess.preprocess_initial(dataframe)

template.create_custom_theme()
template.set_default_theme()

app.layout = html.Div(
    className="content",
    children=[
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
                                            children="Nombre de Tik Tok postés ce mois",
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
                        html.Img(
                            src="/assets/circle.png",
                            style={
                                "position": "relative",
                                "top": "-70px",
                                "height": "200px",
                                "width": "200px",
                                "padding": "10px",
                                "margin-left": "150px",
                                "margin-top": "30px",
                            },
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
                        ),
                        html.Button(
                            "Partages",
                            id="par-btn",
                            style={
                                "font-size": "11px",
                                "backgroundColor": "white",
                                "color": "black",
                                "width": "140px",
                                "border": "1.5px black solid",
                                "height": "40px",
                                "text-align": "center",
                            },
                        ),
                    ],
                    style={"width": "150px"},
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[],
                        ),
                        dcc.Graph(
                            id="line-chart",
                            className="graph",
                            figure=line_chart.get_empty_figure(),
                            config=dict(
                                scrollZoom=False,
                                showTips=False,
                                showAxisDragHandles=False,
                                doubleClick=False,
                                displayModeBar=False,
                            ),
                        ),
                    ]
                ),
                dcc.Graph(
                    id="heatmap",
                    className="graph",
                    figure=line_chart.get_empty_figure(),
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False,
                    ),
                ),
            ],
        ),
        html.Footer(
            children=[
                html.Div(
                    [
                        html.Button(
                            "Médias",
                            id="media-btn",
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
                        ),
                        html.Button(
                            "Sujets",
                            id="sujet-btn",
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
                        ),
                    ]
                ),
            ]
        ),
    ],
)


@app.callback(
    Output("container-button-basic", "children"),
    Input("submit-val", "n_clicks"),
    State("input-on-submit", "value"),
)
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value, n_clicks
    )
