"""
    This file contains the code for the bubble plot.
"""

import plotly.express as px


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
        log_x=True,
        log_y=True,
        range_x=gdp_range,
        range_y=co2_range,
        color_discrete_sequence=px.colors.sequential.ice,
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
