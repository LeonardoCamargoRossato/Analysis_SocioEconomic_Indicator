from libraries import px, go, np, make_subplots
from colors_countries_and_regions import *

# Plots Census2010 data against specified axes with trendline and color customization
def Plot_Scatter(df, axis_x, axis_y, cor, hovername,country):
    fig = px.scatter(data_frame=df, x=axis_x, y=axis_y, color=cor, 
                     marginal_x="box", marginal_y="box", hover_name=hovername,
                     template="simple_white",
                     log_x=True,log_y=True,height=500,width=800
                    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis={
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        yaxis={
            'title_font': {'color': 'black'},
            'tickfont': {'color': 'black'}
        },
        legend={
            'font': {'color': 'black'},
            'orientation': "h",  
            'xanchor': "center",  
            'x': 0.5, 'y': 1.2  
        }
    )
    return fig


# def Plot_Scatter(df, axis_x, axis_y, cor, hovername, country):
#     # Obter o dicionário de cores para o país
#     if country in macrorregion_color_map:
#         color_map = macrorregion_color_map[country]
#     else:
#         raise ValueError(f"As cores para o país '{country}' não estão definidas.")

#     # Criar o subplot para scatter plot
#     fig = make_subplots(
#         rows=1, cols=1, 
#         shared_xaxes=True
#     )
    
#     # Adicionar os pontos do scatter plot com as cores mapeadas
#     unique_colors = df[cor].unique()
#     for category in unique_colors:
#         if category in color_map:
#             category_color = color_map[category]
#         else:
#             category_color = "#000000"  # Cor padrão para valores não encontrados
        
#         filtered_df = df[df[cor] == category]
#         fig.add_trace(
#             go.Scatter(
#                 x=filtered_df[axis_x],
#                 y=filtered_df[axis_y],
#                 mode='markers',
#                 name=str(category),
#                 marker=dict(color=category_color),
#                 text=filtered_df[hovername]
#             )
#         )
    
#     # Calcular a trendline usando numpy.polyfit
#     x_vals = df[axis_x]
#     y_vals = df[axis_y]
#     trendline = np.polyfit(np.log(x_vals), np.log(y_vals), 1)
#     trend_x = np.linspace(x_vals.min(), x_vals.max(), 100)
#     trend_y = np.exp(trendline[1]) * trend_x**trendline[0]
    
#     # Adicionar a trendline
#     fig.add_trace(
#         go.Scatter(
#             x=trend_x, y=trend_y, mode='lines',
#             name="Trendline", line=dict(color="black", dash="dash")
#         )
#     )
    
#     # Configuração do layout
#     fig.update_layout(
#         plot_bgcolor='white',
#         paper_bgcolor='white',
#         xaxis=dict(
#             title=axis_x,
#             title_font=dict(color='black'),
#             tickfont=dict(color='black'),
#             type="log"  # Eixo X em escala log
#         ),
#         yaxis=dict(
#             title=axis_y,
#             title_font=dict(color='black'),
#             tickfont=dict(color='black'),
#             type="log" 
#         ),
#         legend=dict(
#             font=dict(color='black'),
#             orientation="h", 
#             xanchor="center",  
#             x=0.5, y=1.15
#         ),
#         height=500, width=800, title_text="Scatter Plot with Log Trendline", title_x=0.5
#     )
    
#     return fig





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

#
#
#
#
################################################################################################
#  Cities Compare Code Functions
################################################################################################
#
#
#
#

def get_country_info(country):
    """
    Given a country name, returns a dictionary with country-specific column mappings.

    Args:
        country (str): Name of the country.

    Returns:
        dict: Dictionary containing keys `index_axis_x`, `index_axis_y`, `index_state_column`, and `index_hovername`.
    """
    if country == 'Brazil':
        return {
            'index_axis_x': 'Total_Pop_Absol',
            'index_axis_y': 'IDHM_2010',
            'index_state_column': 'UF',
            'index_hovername': 'Municipio'
        }
    elif country == 'USA':
        return {
            'index_axis_x': '2015_Tract_population',
            'index_axis_y': 'unadjusted_hdi',
            'index_state_column': 'State',
            'index_hovername': 'County_States'
        }
    elif country == 'Peru':
        return {
            'index_axis_x': 'Pop_2017',
            'index_axis_y': 'HDI_2017',
            'index_state_column': 'State',
            'index_hovername': 'City'
        }
    elif country == 'Mexico':
        return {
            'index_axis_x': 'Pop_Total_2010',
            'index_axis_y': 'IDH_2000',
            'index_state_column': 'State',
            'index_hovername': 'Hovername'
        }
    elif country == 'El Salvador':
        return {
            'index_axis_x': 'Pop_total_2005',
            'index_axis_y': 'IDH_2005',
            'index_state_column': 'State',
            'index_hovername': 'Comuna'
        }
    elif country == 'Chile':
        return {
            'index_axis_x': 'Población_2017',
            'index_axis_y': 'IDC_2020',
            'index_state_column': 'REGIÓN',
            'index_hovername': 'COMUNA'
        }
    else:
        return {
            'index_axis_x': None,
            'index_axis_y': None,
            'index_state_column': None,
            'index_hovername': None
        }
    
def create_interactive_scatter_go(df, axis_x, axis_y, hovername_city_column, color_city, color_country, selected_city):
    # Filter valid values for logarithmic scale
    df = df[(df[axis_x] > 0) & (df[axis_y] > 0)]

    # Create the base figure
    fig = go.Figure()

    fig.add_trace( go.Scatter(x=df[axis_x], y=df[axis_y], mode='markers', marker=dict(color=color_country, size=8),
                              name="All Cities", text=df[hovername_city_column], hoverinfo="text",
                             )
                 )
    # Filter data for the selected city
    selected_city_data = df[df[hovername_city_column] == selected_city]

    if not selected_city_data.empty:
        fig.add_trace(
            go.Scatter(
                x=selected_city_data[axis_x],
                y=selected_city_data[axis_y],
                mode="markers",
                marker=dict(symbol="star", size=15, color="white", line=dict(color="black", width=2)),
                name="Selected City",
                text=selected_city_data[hovername_city_column],
                hoverinfo="text",
            )
        )
    else:
        print(f"No valid data to plot for selected city: {selected_city}")

    # Layout settings
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", height=400, width=600,
        xaxis=dict(title=axis_x, type="log", showgrid=True, gridcolor="black", title_font=dict(color="black"), tickfont=dict(color="black")),
        yaxis=dict(title=axis_y, type="log", showgrid=True, gridcolor="black", title_font=dict(color="black"), tickfont=dict(color="black")),
        legend=dict(title=dict(text="Legend", font=dict(color="black")), orientation="v", font=dict(color="black"), yanchor="bottom", 
                    y=-1.0, xanchor="center", x=0.5)
    )

    return fig

