'''
    Contains the template to use in the data visualization.
'''
import plotly.graph_objects as go
import plotly.io as pio


THEME = {
    'background_color': '#ffffff',
    'font_family': 'Roboto',
    'accent_font_family': 'Roboto Slab',
    'dark_color': '#2A2B2E',
    'pale_color': '#DFD9E2',
    'line_chart_color': 'black',
    'label_font_size': 14,
    'label_background_color': '#ffffff',
    'colorscale': 'Bluyl'
}



def create_custom_theme():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary, using the dark
        color.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Sets the line chart's line color to the one
        designated in the THEME dictionary. Also sets
        the color scale to be used by the heatmap
        to the one in the THEME dictionary.

        Specifies the x-axis ticks are tilted 45
        degrees to the right.
    '''
    # TODO : Generate template described above
    pio.templates['new_theme'] = go.layout.Template(
        layout=go.Layout(
            font_color=THEME['dark_color'],
            font_family=THEME['font_family'],
            
            paper_bgcolor=THEME['background_color'],
            plot_bgcolor=THEME['background_color'],
        
            hoverlabel=dict(
                bgcolor=THEME['label_background_color'],
                font_size=THEME['label_font_size'],
                font_color=THEME['dark_color']),
            
            hovermode = 'closest',
            colorscale = dict(sequential=THEME['colorscale']),
            colorway = [THEME['line_chart_color']],
            xaxis = dict(
                        tickangle = -45,
                        tickmode = 'array',
                    )
        )
    )

def set_default_theme():
    '''
        Sets the default theme to be a combination of the
        'plotly_white' theme and our custom theme.
    '''
    template=pio.templates['plotly_white+new_theme']
    pio.templates.default = template
