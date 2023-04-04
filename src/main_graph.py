'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import preprocess

def get_figure(data, group_by_column, metric, year):
    '''
        Function to get the figure with given metrics

        data is the complete data
        metric is the metric of magitude to use in the graph, it can be either 'nbVues', 'nbCommentaires', 'nbLikes' or 'nbPartages'
        group_by_column is the column to consider, it can be either "compte", "durée" ou "tags"
        year is the year(s) to display, it can be either 2019, 2020, 2021, 2022 or "all"
    '''

    if data is None or metric is None or group_by_column is None or year is None:
        return get_empty_figure()
    
    data_to_display  = preprocess.bubble_graph(data, group_by_column, year)

    if group_by_column == 'durée':
        return bar_chart(data_to_display, group_by_column, metric)
    else :
        return treemap_chart(data_to_display, group_by_column, metric)
    

def bar_chart(data, group_by_column, metric):
    return px.bar(data, x=group_by_column, y=metric)

def treemap_chart(data, group_by_column, metric):
    if group_by_column == 'compte':   
        fig = px.treemap(
            data, 
            path=[px.Constant("Graph title"), "pays", group_by_column], 
            values = metric,
        )
        fig.update_traces(root_color="lightgrey")
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        return fig

    if group_by_column == 'tags':
        fig = px.treemap(
            data, 
            path=[px.Constant("Graph title"), group_by_column], 
            values = metric,
        )
        fig.update_traces(root_color="lightgrey")
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        return fig


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
                        "text": "Cliquer sur un des boutons en bas pour plus d'informations",
                        "showarrow": False
                        }
                ],
                dragmode = False,
            )
    
    return fig