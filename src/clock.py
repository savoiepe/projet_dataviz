import plotly.graph_objects as go
import pandas as pd


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
            text="Heure propice pour publier",
            x=0.5,  # Center title
            y=0.2,  # Place title below the plot
            font=dict(
                size=15,
                color="black",
            ),
        ),
        polar=dict(
            #bgcolor="rgba(0,0,0,0)",  # Remove grey background
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
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig
