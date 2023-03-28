'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(data, x=list(data.columns.year), y=data.index, labels=dict(color='Trees'))
    fig.update_layout(yaxis={"title": 'Neighborhood', "visible": False},
                    xaxis = dict(
                        title = 'Year',
                        tickmode = 'array',
                        tickvals = list(data.columns.year),
                        visible = False
                    ),
                    showlegend=False,

                )
    fig.update_traces(hovertemplate= hover_template.get_heatmap_hover_template())
    return fig
