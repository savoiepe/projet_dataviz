# -*- coding: utf-8 -*-

"""
    File name: app.py
    Author: Olivia Gélinas
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
import heatmap
import line_chart
import template


app = dash.Dash(__name__)
app.title = "TP3 | INF8808"

dataframe = pd.read_csv("./assets/data/arbres.csv")

dataframe = preprocess.convert_dates(dataframe)
dataframe = preprocess.filter_years(dataframe, 2010, 2020)
yearly_df = preprocess.summarize_yearly_counts(dataframe)
data = preprocess.restructure_df(yearly_df)

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
                            figure=line_chart.fig_test(yearly_df),
                            config=dict(
                                scrollZoom=False,
                                showTips=False,
                                showAxisDragHandles=False,
                                doubleClick=False,
                                displayModeBar=False,
                            ),
                            style={
                                "margin-left": "30px",
                                "width": "700px",
                                "height": "700px",
                            },
                        ),
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
                                        "marginLeft": "0",
                                        "marginBottom": "20px",
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
                                        "marginBottom": "20px",
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
                                        "marginBottom": "20px",
                                    },
                                ),
                            ]
                        ),
                    ],
                ),
                dcc.Graph(
                    id="heatmap",
                    className="graph",
                    figure=line_chart.fig_test(yearly_df),
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False,
                    ),
                    style={"margin-left": "30px", "width": "700px", "height": "700px"},
                ),
            ],
        ),
    ],
)


# @app.callback(
#     Output('line-chart', 'figure'),
#     [Input('heatmap', 'clickData')]
# )
# def heatmap_clicked(click_data):
#     '''
#         When a cell in the heatmap is clicked, updates the
#         line chart to show the data for the corresponding
#         neighborhood and year. If there is no data to show,
#         displays a message.

#         Args:
#             The necessary inputs and states to update the
#             line chart.
#         Returns:
#             The necessary output values to update the line
#             chart.
#     '''
#     if click_data is None or click_data['points'][0]['z'] == 0:
#         fig = line_chart.get_empty_figure()
#         return fig

#     arrond = click_data['points'][0]['y']
#     year = click_data['points'][0]['x']

#     line_data = preprocess.get_daily_info(
#         dataframe,
#         arrond,
#         year)

#     line_fig = line_chart.get_figure(line_data, arrond, year)

#     return line_fig

# @app.callback(
#     Output('container-button-basic', 'children'),
#     Input('submit-val', 'n_clicks'),
#     State('input-on-submit', 'value')
# )
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value,
#         n_clicks
#     )
