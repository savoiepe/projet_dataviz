'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import preprocess

def get_figure(data, selected, year):
    '''
        Function to get the figure with given metrics
        data is the complete data
        metric is the metric of magitude to use in the graph, it can be either 'nbVues', 'nbCommentaires', 'nbLikes' or 'nbPartages'
        group_by_column is the column to consider, it can be either "compte", "durée" ou "tags"
        year is the year(s) to display, it can be either 2019, 2020, 2021, 2022 or "all"
    '''

    data_to_display = preprocess.line_graph(data, selected, year)
    fig = px.line(data_to_display, x="date_str", y="n_post")
    if selected is None:
        fig.update_layout(title='Nombre de tiktok posté entre 2019 et 2022',title_x=0.5)
        return fig
    if selected[0]=='durée':
        fig.update_layout(title='Nombre de tiktoks posté de durée '+ selected[1] + ' secondes')
    elif selected[0]=='tags':
        fig.update_layout(title='Nombre de tiktoks posté ayant pour sujet '+ "'" + selected[1] + "'")
    elif selected[0]=='compte':
        fig.update_layout(title='Nombre de tiktoks posté par le média '+ selected[1])
    fig.update_layout(title_x=0.5)
    return fig 
