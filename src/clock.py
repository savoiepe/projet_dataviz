import plotly.graph_objects as go
import pandas as pd
from preprocess import pie_chart


data = pd.DataFrame(
    {
        "hour": range(24),
        "n_post": [
            2,
            5,
            8,
            12,
            15,
            18,
            20,
            22,
            23,
            24,
            25,
            26,
            28,
            29,
            30,
            31,
            32,
            33,
            35,
            34,
            30,
            25,
            20,
            5,
        ],
    }
)


# data = pie_chart(data)


def get_clock(data):

    # set the radial axis range to be the same for all hours
    max_value = max(data["n_post"])
    radial_range = [0, max_value + 5]

    # create a polar chart with 24 sectors
    fig = go.Figure(
        go.Barpolar(
            r=[max_value] * 24,
            theta=data["hour"] * 15,  # each sector is 360/24=15 degrees
            marker=dict(
                color=data["n_post"],
                colorscale="Blues",  # Blues rend mieux que ice je pense
            ),
            width=15,
        )
    )

    # update the layout to make it look like a clock
    fig.update_layout(
        font=dict(
            size=25,
            color="black",
        ),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",  # Transparent background
            radialaxis=dict(
                visible=True,
                range=radial_range,  # set the radial axis range
                tickvals=[0, max_value],  # set the tick values
                showticklabels=False,
            ),
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


fig = get_clock(data)
fig.show()
