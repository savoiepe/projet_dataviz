'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hovertemp = '<b style="font-family:\'Roboto Slab\'">'
    hovertemp += "Neighborhood : " + '</b>' + '<span style="font-family:\'Roboto\'">' +"%{y}" + "</span>"+"<br>"
    hovertemp += '<b style="font-family:\'Roboto Slab\'">'
    hovertemp += "Year : " + '</b>' + '<span style="font-family:\'Roboto\'">' +"%{x}" + "</span>"+"<br>"
    hovertemp += '<b style="font-family:\'Roboto Slab\'">'
    hovertemp += "Tree planted : " + '</b>' + '<span style="font-family:\'Roboto\'">' +"%{z}" + "</span>"+"<br>"
    hovertemp += "<extra></extra>"
    return hovertemp

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hovertemp = '<b style="font-family:\'Roboto Slab\'">'
    hovertemp += "Date : " + '</b>' + '<span style="font-family:\'Roboto\'">' +"%{x}" + "</span>"+"<br>"
    hovertemp += '<b style="font-family:\'Roboto Slab\'">'
    hovertemp += "Trees : " + '</b>' + '<span style="font-family:\'Roboto\'">' +"%{y}" + "</span>"+"<br>"
    hovertemp += "<extra></extra>"
    return hovertemp

