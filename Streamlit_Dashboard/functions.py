from libraries import px
from colors_countries_and_regions import *

# Plots Census2010 data against specified axes with trendline and color customization
def Plot_Scatter(df, axis_x, axis_y, cor, hovername):
    fig = px.scatter(data_frame=df, x=axis_x, y=axis_y, color=cor, trendline='ols', 
                     marginal_x="box", marginal_y="box", hover_name=hovername,
                     template="simple_white",trendline_color_override="black", trendline_options=dict(log_x=True,log_y=True),
                     log_x=True,log_y=True,height=500,width=800
                    )
    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'xaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        'yaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        'legend': {
            'font': {'color': 'black'}
        }
    })
    return fig

# Plots Census2010 data without considering regions and without trendline
def Plot_Scatter_Simple(df, axis_x, axis_y, hovername, color):
    fig = px.scatter(
        data_frame=df, x=axis_x, y=axis_y, marginal_x="box", marginal_y="box",
        template="simple_white", hover_name=hovername, log_x=False, log_y=False,
        height=500, width=800
    )
    # Define a cor fixa para todos os pontos
    fig.update_traces(marker=dict(color=color))
    
    # Layout geral
    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'xaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        'yaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        }
    })
    return fig

# Plots Census2010 data without considering regions, with trendline option
def Plot_Scatter_No_Regions(df, axis_x, axis_y, hovername, color):
    fig = px.scatter(
        data_frame=df, x=axis_x, y=axis_y, marginal_x="box", marginal_y="box",
        trendline_color_override="black", trendline_options=dict(log_x=True,log_y=True), trendline='ols', 
        template="simple_white", hover_name=hovername, log_x=True, log_y=True, height=500, width=1200
    )
    # Define a cor fixa para todos os pontos
    fig.update_traces(marker=dict(color=color))
    
    # Layout geral
    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'xaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        'yaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        }
    })
    return fig

# Plots Census2010 data without trendline
def Plot_Scatter_No_Trendline(df, axis_x, axis_y, hovername, color):
    fig = px.scatter(
        data_frame=df, x=axis_x, y=axis_y, marginal_x="box", marginal_y="box",
        template="simple_white", hover_name=hovername, log_x=True, log_y=True,
        height=500, width=800
    )
    # Define a cor fixa para todos os pontos
    fig.update_traces(marker=dict(color=color))
    
    # Layout geral
    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'xaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        'yaxis': {
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        }
    })
    return fig

######################################
#    C o l o r s   F u n c t i o n s :
######################################

# Function to list the macrorregions of a country in the dataframe
def country_macrorregions_list(df, country):
    if country in ['Brazil', 'Chile', 'Mexico', 'ElSalvador']:
        return [list(df.Macroregioes.unique()), 'Macroregioes']
    elif country == 'USA':
        return [list(df.Macroregion.unique()), 'Macroregion']
    elif country == 'Peru':
        return [list(df.Macroregioes_Topografica.unique()), 'Macroregioes_Topografica']

# Function to list the states of a country in the dataframe
def country_states_list(df, country):
    if country in ['Brazil']:
        return [list(df.UF.unique()), 'UF']
    elif country in ['USA', 'Mexico', 'Peru', 'ElSalvador']:
        return [list(df.State.unique()), 'State']
    elif country == 'Chile':
        return [list(df['REGIÓN'].unique()), 'REGIÓN']

# Function to select the color of a country
def select_color_country(country):
    return country_colors[country]

# Function to select all macrorregion colors of a country
def select_color_all_macrorregions_country(country):
    if country in macrorregion_color_map:
        # Return the list of colors for all macrorregions in the country
        return list(macrorregion_color_map[country].values())
    else:
        raise ValueError(f"The country '{country}' does not have defined colors for macrorregions.")

# Function to select the color of a specific macrorregion in a country
def select_color_one_macrorregion_country(country, macrorregion):
    if country in macrorregion_color_map:
        macrorregion_colors = macrorregion_color_map[country]
        # Check if the macrorregion exists in the country
        if macrorregion in macrorregion_colors:
            return macrorregion_colors[macrorregion]
        else:
            raise ValueError(f"The macrorregion '{macrorregion}' does not exist for the country '{country}'.")
    else:
        raise ValueError(f"The country '{country}' does not have defined colors for macrorregions.")

# Function to select all state colors of a country
def select_color_all_state_country(country):
    if country in state_color_mapping_countries:
        # Return the list of colors for all states in the country
        return list(state_color_mapping_countries[country].values())
    else:
        raise ValueError(f"The country '{country}' does not have defined colors for states.")

# Function to select the color of a specific state in a country
def select_color_one_state_country(country, state):
    if country in state_color_mapping_countries:
        # Check if the state exists in the country
        if state in state_color_mapping_countries[country]:
            return state_color_mapping_countries[country][state]
        else:
            raise ValueError(f"The state '{state}' does not exist for the country '{country}'.")
    else:
        raise ValueError(f"The country '{country}' does not have defined colors for states.")


# Function to list the macrorregions of a country
def get_macrorregions_list(country):
    """
    Returns the list of a country's macrorregions with the country's name as the first element.
    """
    if country in macrorregion_color_map:
        macrorregions = list(macrorregion_color_map[country].keys())  # Gets the keys (macrorregion names)
        macrorregions = [region for region in macrorregions if region != 'nan']  # Removes 'nan' entries
        return [country] + macrorregions  # Adds the country's name as the first element
    else:
        raise ValueError(f"The country '{country}' does not have defined macrorregions.")

