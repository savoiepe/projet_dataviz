"""
    This file contains the code for the bubble plot.
"""

import plotly.express as px
import hover_template


def get_plot(my_df, gdp_range, co2_range):
    """
    Generates the bubble plot.

    The x and y axes are log scaled, and there is
    an animation between the data for years 2000 and 2015.

    The discrete color scale (sequence) to use is Set1 (see : https://plotly.com/python/discrete-color/)

    The markers' maximum size is 30 and their minimum
    size is 6.

    Args:
        my_df: The dataframe to display
        gdp_range: The range for the x axis
        co2_range: The range for the y axis
    Returns:
        The generated figure
    """
    # Create the scatter plot
    fig = px.scatter(
        my_df,
        x="GDP",
        y="CO2",
        animation_frame="Year",
        animation_group="Country Name",
        custom_data=["Country Name"],
        size="Population",
        color="Continent",
        size_max=30,
        # size_min=6,
        log_x=True,
        log_y=True,
        range_x=gdp_range,
        range_y=co2_range,
        color_discrete_sequence=px.colors.qualitative.Set1,
    )

    fig.update_traces(hovertemplate=hover_template.get_bubble_hover_template())

    return fig


def update_animation_hover_template(fig):
    """
    Sets the hover template of the figure,
    as well as the hover template of each
    trace of each animation frame of the figure

    Args:
        fig: The figure to update
    Returns:
        The updated figure
    """
    fig.update_layout(hovermode="closest")
    for frame in fig.frames:
        for trace in frame.data:
            trace.update(hovertemplate=hover_template.get_bubble_hover_template())
    return fig


def update_animation_menu(fig):
    """
    Updates the animation menu to show the current year, and to remove
    the unnecessary 'Stop' button.

    Args:
        fig: The figure containing the menu to update
    Returns
        The updated figure
    """
    # Update the animation menu
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            dict(
                                frame=dict(duration=200, redraw=False),
                                fromcurrent=True,
                            ),
                        ],
                    ),
                    dict(
                        label="Pause",
                        method="animate",
                        args=[
                            [None],
                            dict(
                                transition=dict(duration=0),
                                frame=dict(duration=0, redraw=False),
                            ),
                        ],
                    ),
                ],
            ),
            dict(
                type="buttons",
                showactive=True,
                buttons=[
                    dict(
                        label="2000",
                        method="animate",
                        args=[
                            None,
                            dict(
                                frame=dict(duration=0, redraw=False),
                                transition=dict(duration=0),
                                fromcurrent=True,
                                args=[
                                    [0],
                                    dict(
                                        frame=dict(duration=0, redraw=True),
                                        transition=dict(duration=0),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        label="2015",
                        method="animate",
                        args=[
                            None,
                            dict(
                                frame=dict(duration=0, redraw=False),
                                transition=dict(duration=0),
                                fromcurrent=True,
                                args=[
                                    [1],
                                    dict(
                                        frame=dict(duration=0, redraw=True),
                                        transition=dict(duration=0),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ]
    )

    return fig


def update_axes_labels(fig):
    """
    Updates the axes labels with their corresponding titles.

    Args:
        fig: The figure to be updated
    Returns:
        The updated figure
    """
    fig.update_layout(
        xaxis_title="GDP per capita ($ USD)",
        yaxis_title="CO2 emissions per capita (metric tonnes)",
    )
    return fig


def update_template(fig):
    """
    Updates the layout of the figure, setting
    its template to 'simple_white'

    Args:
        fig: The figure to update
    Returns
        The updated figure
    """
    fig.update_layout(template="simple_white")
    return fig


def update_legend(fig):
    """
    Updated the legend title

    Args:
        fig: The figure to be updated
    Returns:
        The updated figure
    """
    fig.update_layout(legend=dict(title="Legend"))
    return fig
