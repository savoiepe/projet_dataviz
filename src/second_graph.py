'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import preprocess

def get_figure(data, selected, year):
    '''
        Function to get the figure with given metrics
        data is the complete data
        selected is the metric of magitude to use in the graph, it can be either 'nbVues', 'nbCommentaires', 'nbLikes' or 'nbPartages'
        group_by_column is the column to consider, it can be either "compte", "durée" ou "tags"
        year is the year(s) to display, it can be either 2019, 2020, 2021, 2022 or "all"
    '''
    
    data_to_display = preprocess.line_graph(data, selected, year)
    fig = px.line(data_to_display, x="date_str", y="n_post")
    fig.update_xaxes(
    showticklabels=True,
    tickformat='%Y-%m',
    ticklen=10,
    tickangle=0,
    showgrid=False,
    showline=True,
    linewidth=1,
    linecolor='black',
    mirror=True
)   
    
    fig.update_yaxes(showgrid=False,
                     showline=True,
                     mirror=True,
                     linewidth=1,
                     linecolor='black')

    fig = add_covid_info(fig)

    
    
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




def add_covid_info(fig):
        # Display COVID lines
    fig.add_shape(
        type='line',
        x0='2020-03-01', x1='2020-03-01', xref='x', y0=0, y1=1, yref='paper',
        line=dict(color='red', width=2, dash='dash')
    )

    fig.add_shape(
        type='line',
        x0='2022-03-01', x1='2022-03-01', xref='x', y0=0, y1=1, yref='paper',
        line=dict(color='green', width=2, dash='dash')
    )
    # Legend of the COVID lines
    fig.add_shape(
        type='rect',
        x0=0.05, x1=0.28, xref='paper', y0=0.82, y1=0.95, yref='paper',
        fillcolor='white', line=dict(color='black', width=1)
    )
    fig.add_shape(
        type='line',
        x0=0.06, x1=0.12, xref='paper', y0=0.91, y1=0.91, yref='paper',
        line=dict(color='red', width=2, dash='dash')
    )
    
    fig.add_annotation(
        text='Début COVID', xref='paper', yref='paper',
        x=0.12, y=0.94, showarrow=False
    )
    
    fig.add_shape(
        type='line',
        x0=0.06, x1=0.12, xref='paper', y0=0.85, y1=0.85, yref='paper',
        line=dict(color='green', width=2, dash='dash')
    )
    
    fig.add_annotation(
        text='Fin COVID', xref='paper', yref='paper',
        x=0.12, y=0.88, showarrow=False
    )
    
    return fig