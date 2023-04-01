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

import pandas as pd

import preprocess
import main_chart
import clock
import template


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
                        )
                    ]
                ),
                dcc.Graph(
                    id="bubble_graph",
                    className="graph",
                    figure=main_chart.get_figure(dataframe, 'nbVues', 'tags', 'all'),
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
