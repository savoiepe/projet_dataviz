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

    max_value = max(data["n_post"])
    radial_range = [0, max_value + 5]

    fig = go.Figure(
        go.Barpolar(
            r=[max_value] * 24,
            theta=data["hour"] * 15,  # each sector is 360/24=15 degrees
            marker=dict(
                color=data["n_post"],
                colorscale="Blues",  # Set a blue color (must be modified)
            ),
            width=15,
        )
    )

    fig.update_layout(
        title=dict(
            text="Heure propice pour poster",
            x=0.5,  # Center title
            y=0.02,  # Place title below the plot
            font=dict(
                size=20,
                color="black",
            ),
        ),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",  # Remove grey background
            radialaxis=dict(
                visible=True,
                range=radial_range,
                tickvals=[0, max_value],
                showticklabels=False,
            ),
            angularaxis=dict(
                visible=True,
                tickmode="array",
                tickvals=[i * 15 for i in range(24)],
                ticktext=[str(i) for i in range(24)],
                rotation=90,
                direction="clockwise",
                ticklen=80,  # Should put the tick labels closer to the clock
                tickfont=dict(size=18),
            ),
        ),
    )
    return fig


fig = get_clock(data)
fig.show()
