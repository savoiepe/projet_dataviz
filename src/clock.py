import plotly.graph_objects as go
import pandas as pd


def get_plot(my_df):
    # create a polar chart with 24 sectors
    fig = go.Figure(
        go.Barpolar(
            r=my_df["value"],
            theta=my_df["hour"] * 15,  # each sector is 360/24=15 degrees
            marker=dict(
                color=my_df["value"],
                colorscale="Blues",
                showscale=True,
                colorbar=my_df(
                    tickvals=[min(my_df["value"]), max(my_df["value"])],
                    ticktext=["Low", "High"],
                ),
            ),
        )
    )

    # update the layout to make it look like a clock
    fig.update_layout(
        title="Hourly Data",
        font=dict(
            size=16,
            color="black",
        ),
        polar=dict(
            radialaxis=dict(visible=False, range=[0, max(my_df["value"])]),
            angularaxis=dict(
                visible=True,
                tickmode="array",
                tickvals=[i * 15 for i in range(24)],
                ticktext=[str(i) for i in range(24)],
                rotation=90,
                direction="clockwise",
            ),
        ),
    )

    return fig
