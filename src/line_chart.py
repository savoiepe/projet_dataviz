'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    fig = px.line()
    fig.update_xaxes(range = [0,1])
    fig.update_yaxes(range = [0,1])
    fig.update_layout(
                {
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)'},
                xaxis =  {"visible": False },
                yaxis = { "visible": False },
                annotations = [
                    {   
                        "text": "Cliquer sur un des boutons à gauches pour plus d'informations",
                        "showarrow": False
                        }
                ],
                dragmode = False,
            )
    
    return fig


# def add_rectangle_shape(fig):
#     '''
#         Adds a rectangle to the figure displayed
#         behind the informational text. The color
#         is the 'pale_color' in the THEME dictionary.

#         The rectangle's width takes up the entire
#         paper of the figure. The height goes from
#         0.25% to 0.75% the height of the figure.
#     '''
#     # TODO : Draw the rectangle
    
#     fig.update_layout(shapes=[
#         dict(
#             type="rect",
#             xref="x",
#             yref="y",
#             x0=0,
#             y0=0.25,
#             x1=1,
#             y1=0.75,
#             fillcolor=THEME['pale_color'],
#             line_width=0
#         )
#     ])
#     return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template

    line_data.set_index("index", inplace = True)    
    
    if len(line_data)==1:
        line_fig=px.scatter(line_data, x=line_data.index, y=line_data.Counts)
    elif len(line_data) > 1:
        line_fig= px.line(line_data, x=line_data.index, y=line_data.Counts)

    line_fig.update_layout(
        title='Trees Planted in ' + str(arrond) + " in " + str(year),
        yaxis={"title": 'Trees'},
        xaxis = dict(
                tickmode = 'array',
                tickformat = '%d %b'
            ),
        xaxis_title=None,
        dragmode=False)
    
    line_fig.update_traces(hovertemplate= hover_template.get_linechart_hover_template())
    
    return line_fig
