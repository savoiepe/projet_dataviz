"""
    Contains some functions related to the creation of the line chart.
"""
import plotly.express as px
import preprocess
import datetime


def get_figure(data, selected, year):
    """
    Function to get the figure with given metrics
    data is the complete data
    selected is the metric of magitude to use in the graph, it can be either 'nbVues', 'nbCommentaires', 'nbLikes' or 'nbPartages'
    group_by_column is the column to consider, it can be either "compte", "durée" ou "tags"
    year is the year(s) to display, it can be either 2019, 2020, 2021, 2022 or "all"
    """
    start_year, end_year = year.split("-")

    data_to_display = preprocess.line_graph(data, selected, year)
    min_date = min(data_to_display['date_str'])
    max_date = max(data_to_display['date_str'])

    fig = px.line(data_to_display, x="date_str", y="n_post")

    fig.update_traces(
        hovertemplate="<b>Date:</b> %{x}<br><b>Nombre de posts:</b> %{y}<extra></extra>"
    )

    fig.update_xaxes(
        title="",
        showticklabels=True,
        ticks="outside",
        tickfont=dict(
            family="Arial",
            size=12,
            color="rgb(82, 82, 82)",
        ),
        tickformat="%Y-%m",
        tickangle=0,
        showgrid=False,
        showline=True,
        linewidth=1,
        linecolor="black",
        mirror=True,
        tickson="boundaries",
    )

    fig.update_yaxes(
        title="",
        showticklabels=True,
        ticks="outside",
        tickfont=dict(
            family="Arial",
            size=12,
        ),
        showgrid=False,
        showline=True,
        mirror=True,
        linewidth=1,
        linecolor="black",
        rangemode="tozero",
    )

    fig = add_covid_info(fig, min_date, max_date)
    # Affichage des titres et definition des couleurs des graphiques de droite
    if selected is None:
        if start_year != end_year:
            fig.update_layout(
                title="Nombre de tiktok posté entre {} et {}".format(
                    start_year, end_year
                ),
                title_x=0.5,
            )
        else:
            fig.update_layout(
                title="Nombre de tiktok posté en {}".format(start_year), title_x=0.5
            )
        fig.update_traces(line_color="rgb(50, 141, 207)")
        return fig
    if selected[0] == "durée":
        fig.update_layout(
            title="Nombre de tiktoks posté de durée " + selected[1] + " secondes"
        )
        fig.update_traces(line_color="rgb(50, 141, 207)")
    elif selected[0] == "tags":
        fig.update_layout(
            title="Nombre de tiktoks posté ayant pour sujet " + "'" + selected[1] + "'"
        )
        fig.update_traces(line_color="rgb(50, 141, 207)")
    elif selected[0] == "compte":
        fig.update_layout(title="Nombre de tiktoks posté par le média " + selected[1])
        fig.update_traces(line_color="rgb(50, 141, 207)")
    elif selected[0] == "pays":
        if selected[1] == "Canada":
            fig.update_layout(
                title="Nombre de tiktoks posté par les médias du " + selected[1]
            )
        else:
            fig.update_layout(
                title="Nombre de tiktoks posté par les médias de " + selected[1]
            )
        fig.update_traces(line_color="rgb(50, 141, 207)")
    fig.update_layout(title_x=0.5)
    return fig


def add_covid_info(fig, start, end):
    print(end)
    start_date = datetime.datetime.strptime(start, "%Y-%m")
    end_date = datetime.datetime.strptime(end, "%Y-%m")
    start_covid = datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")
    end_covid = datetime.datetime.strptime("2022-03-01", "%Y-%m-%d")

    display_start_covid = start_date < start_covid and end_date > start_covid
    display_end_covid = start_date < end_covid and end_date > end_covid

    if display_start_covid:
        # Covid start line on the figure
        fig.add_shape(
            type="line",
            x0="2020-03-01",
            x1="2020-03-01",
            xref="x",
            y0=0,
            y1=1,
            yref="paper",
            line=dict(color="red", width=2, dash="dash"),
        )

        if display_end_covid:
            # Big rectangle
            fig.add_shape(
                type="rect",
                x0=0.02,
                x1=0.25,
                xref="paper",
                y0=0.82,
                y1=0.95,
                yref="paper",
                fillcolor="white",
                line=dict(color="black", width=1),
            )

        else:
            # Small rectangle
            fig.add_shape(
                type="rect",
                x0=0.02,
                x1=0.25,
                xref="paper",
                y0=0.87,
                y1=0.95,
                yref="paper",
                fillcolor="white",
                line=dict(color="black", width=1),
            )

        # Short dash line in the rectangle
        fig.add_shape(
            type="line",
            x0=0.03,
            x1=0.09,
            xref="paper",
            y0=0.91,
            y1=0.91,
            yref="paper",
            line=dict(color="red", width=2, dash="dash"),
        )

        # Text in rectangle
        fig.add_annotation(
            text="Début COVID",
            xref="paper",
            yref="paper",
            x=0.09,
            y=0.94,
            showarrow=False,
        )

    if display_end_covid:
        # Line on the figure
        fig.add_shape(
            type="line",
            x0="2022-03-01",
            x1="2022-03-01",
            xref="x",
            y0=0,
            y1=1,
            yref="paper",
            line=dict(color="green", width=2, dash="dash"),
        )

        if not display_start_covid:
            # Small rectangle
            fig.add_shape(
                type="rect",
                x0=0.02,
                x1=0.25,
                xref="paper",
                y0=0.87,
                y1=0.95,
                yref="paper",
                fillcolor="white",
                line=dict(color="black", width=1),
            )

        # Display the covid end informations under the covid start informations
        if display_start_covid:
            # Short dash line in the rectangle
            fig.add_shape(
                type="line",
                x0=0.03,
                x1=0.09,
                xref="paper",
                y0=0.85,
                y1=0.85,
                yref="paper",
                line=dict(color="green", width=2, dash="dash"),
            )

            # Text in rectangle
            fig.add_annotation(
                text="Fin COVID",
                xref="paper",
                yref="paper",
                x=0.09,
                y=0.88,
                showarrow=False,
            )
        else:
            # Short dash line in the rectangle
            fig.add_shape(
                type="line",
                x0=0.03,
                x1=0.09,
                xref="paper",
                y0=0.91,
                y1=0.91,
                yref="paper",
                line=dict(color="green", width=2, dash="dash"),
            )

            # Text in rectangle
            fig.add_annotation(
                text="Fin COVID",
                xref="paper",
                yref="paper",
                x=0.09,
                y=0.94,
                showarrow=False,
            )

    return fig
