from libraries import *
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

#
#
#
#
################################################################################################
#  B i n s c a t t e r s     P r o c e s s
################################################################################################
#
#
#
#

# Function to separate data into linear bins
def separate_bins_by_n_values(n, df, axis_x):
    min_value = df[axis_x].min()
    max_value = df[axis_x].max()
    return [min_value + i * (max_value - min_value) / n for i in range(n + 1)]

# Function to separate data into exponential bins
def separate_bins_by_exponential(n, df, axis_x):
    bins = [df[axis_x].min()]
    for i in range(10 * n):
        bins.append(bins[i] * (np.e ** ((i + 1) / n) / np.e ** (i / n)))
    return bins

# Function to create a DataFrame based on bins and calculate the mean of each bin
def create_bins_df(n, df, bin_separation_mode, axis_x, axis_y):
    if bin_separation_mode == 'linear':
        classes = separate_bins_by_n_values(n, df, axis_x)
    elif bin_separation_mode == 'exponential':
        classes = separate_bins_by_exponential(n, df, axis_x)
    df['bins'] = pd.cut(df[axis_x], bins=classes, include_lowest=True,
                        labels=['bin_' + str(i) for i in range(len(classes) - 1)])
    df_bins = df.groupby('bins').agg({axis_x: 'mean', axis_y: 'mean'}).reset_index(drop=True)
    return df_bins

# Function to plot histograms and scatter plots of the bins
def plot_bins_df(df_bins, df, axis_x, axis_y):
    st.write("Data count by bin:")
    st.dataframe(pd.DataFrame(df['bins'].value_counts()).sort_index().T.round(2))
    st.write("Bin averages:")
    st.dataframe(df_bins.T.round(2))
    
    fig = make_subplots(rows=3, cols=1)
    fig.update_layout(title='Analysis ' + axis_y + ' x ' + axis_x + ' by bins',
                      height=1000, width=1000,
                      bargap=0.1, bargroupgap=0.2)
    fig.add_trace(go.Histogram(x=df.sort_values('bins')['bins'], name='Histogram'), row=1, col=1)
    non_nan_x = ~np.isnan(df_bins[axis_x])
    non_nan_y = ~np.isnan(df_bins[axis_y])
    for r in [2, 3]:
        fig.add_trace(go.Scatter(x=df_bins[axis_x][non_nan_x], y=df_bins[axis_y][non_nan_y],
                                 name='Linear Plot'), row=r, col=1)
    fig.update_yaxes(title_text='Counts: number of municipalities in each bin', row=1, col=1)
    fig.update_yaxes(title_text=axis_y + ' mean of bins', row=2, col=1)
    fig.update_xaxes(title_text=axis_x + " mean of bins", type="log", row=3, col=1)
    st.plotly_chart(fig)

# Main function to create and plot graphs based on bins
def create_and_plot_bins_graphs(n, df, bin_separation_mode, axis_x, axis_y):
    df_bins = create_bins_df(n, df, bin_separation_mode, axis_x, axis_y)
    plot_bins_df(df_bins, df, axis_x, axis_y)

#
#
#
################################################
# Route for Calculating Binscatter Curve Fitting
################################################

# Linear fit function (in logarithmic scale)
def linear_func(x, a, b):
    return a * x + b

# Function to plot the graph based on 'bins' and perform curve fitting
def plot_bins_function_fit(df_bins, df, x_axis, y_axis, height=500, width=1000):
    fig = make_subplots()
    
    non_nan_x = ~np.isnan(df_bins[x_axis])
    non_nan_y = ~np.isnan(df_bins[y_axis])
    
    log_x = np.log(df_bins[x_axis][non_nan_x])
    log_y = np.log(df_bins[y_axis][non_nan_y])
    
    # Performing curve fitting
    popt, pcov = curve_fit(linear_func, log_x, log_y)
    y_fit = np.exp(linear_func(log_x, *popt))

    # Incorporating the equation into the legend
    equation_text = f"Fit (y = {popt[0]:.2f}x + {popt[1]:.2f})"
    
    fig.add_trace(go.Scatter(x=df_bins[x_axis][non_nan_x], y=df_bins[y_axis][non_nan_y], 
                             mode='markers+lines', name='Data'))
    fig.add_trace(go.Scatter(x=df_bins[x_axis][non_nan_x], y=y_fit, mode='lines', 
                             name=equation_text, line=dict(color='red')))
    
    fig.update_yaxes(title_text=f"Mean {y_axis} of the bins", type="log")
    fig.update_xaxes(title_text=f"Mean {x_axis} of the bins", type="log")
    fig.update_layout(template="simple_white", height=height, width=width)
    
    st.plotly_chart(fig)


# Function to visualize interactive scatter plot
def plot_interact(x_axis, y_axis, color, hover_name, df, height=500, width=1000):
    fig = px.scatter(data_frame=df, x=x_axis, y=y_axis, color=color, hover_name=hover_name,
                     log_x=True, log_y=True, template="simple_white", height=height, width=width)

    log_x = np.log(df[x_axis])
    log_y = np.log(df[y_axis])

    model = sm.OLS(log_y, sm.add_constant(log_x)).fit()
    predicted = model.predict(sm.add_constant(log_x))

    fig.add_trace(go.Scatter(x=df[x_axis], y=np.exp(predicted), mode='lines',
                             line=dict(color='black'), name="OLS Fit"))

    st.plotly_chart(fig)

# Main function to create and plot graphs based on 'bins'
def binscatter_and_fit_curve(n, df, bin_separation_mode, x_axis, y_axis, height=500, width=1000):
    df_bins = create_bins_df(n, df, bin_separation_mode, x_axis, y_axis)
    plot_bins_function_fit(df_bins, df, x_axis, y_axis, height, width)

################################################
# Binscatter and Scatter: comparison ilustration
################################################

# Function to plot the graph based on 'bins' and perform curve fitting
def plot_df_bins(df_bins, df, x_axis, y_axis, height, width, opacity):
    fig = make_subplots()
    
    # Adding scatter plot for all points
    fig.add_trace(go.Scatter(x=df[x_axis], y=df[y_axis], mode='markers', 
                             marker=dict(color='black', opacity=opacity),
                             name='All Points'))
    
    non_nan_x = ~np.isnan(df_bins[x_axis])
    non_nan_y = ~np.isnan(df_bins[y_axis])
    
    log_x = np.log(df_bins[x_axis][non_nan_x])
    log_y = np.log(df_bins[y_axis][non_nan_y])
    
    # Finding the index of the lowest y-axis value
    idx_min_y = np.argmin(log_y)
    
    # Using only points from the lowest value onwards for fitting
    log_x_adjusted = log_x[idx_min_y:]
    log_y_adjusted = log_y[idx_min_y:]
    
    # Performing curve fitting with adjusted points
    popt, pcov = curve_fit(linear_func, log_x_adjusted, log_y_adjusted)
    
    # Defining x and y values for the fitted line
    x_fit = np.linspace(log_x_adjusted.iloc[0], max(log_x_adjusted), 100)
    y_fit = linear_func(x_fit, *popt)

    # Incorporating equation into the legend
    C = np.exp(popt[1])
    equation_text = f"Fit: y = {C:.2f}x^{popt[0]:.2f}"
    
    fig.add_trace(go.Scatter(x=df_bins[x_axis][non_nan_x], y=df_bins[y_axis][non_nan_y], 
                             mode='markers+lines', name='Data', line=dict(color='blue', dash='dot', width=2), 
                             marker=dict(color='orange', size=8)))
    fig.add_trace(go.Scatter(x=np.exp(x_fit), y=np.exp(y_fit), mode='lines', 
                             name=equation_text, line=dict(color='green', width=1)))

        
    fig.update_yaxes(title_text=y_axis + ' (average in bins)', type="log")
    fig.update_xaxes(title_text=x_axis + " (average in bins)", type="log")
    fig.update_layout(template="simple_white", height=height, width=width)
    
    # Saving figures as SVG and PNG
#     fig.write_image("df_Peru_Bins.svg", scale=3)
#     fig.write_image("df_Peru_Bins.png", scale=3)
    st.plotly_chart(fig)


# Main function to create and plot graphs based on 'bins'
def create_and_plot_bins_graphs__scatter_x_binscatter(n, df, bin_separation_mode, x_axis, y_axis, height, width, opacity):
    df_bins = create_bins_df(n, df, bin_separation_mode, x_axis, y_axis)
    plot_df_bins(df_bins, df, x_axis, y_axis, height, width, opacity)
    
# # Wrapper function for interaction
# def wrapper_plot_interact(x_axis, y_axis, color, hovername, df,height=500, width=1000):
#     return plot_interact(x_axis, y_axis, color, hovername, df, height, width)



#
#
#
#
################################################################################################
# S c a t t e r  G r a p h    P l o t s
################################################################################################
#
#
#
#

#####################
# Base_on_GCA Process
#####################

# Converte uma cor hexadecimal para RGB no formato requerido
def hex_to_rgb(hex_str, opacity=1.0):
    hex_str = hex_str.lstrip("#")  # Remove o '#' inicial, se existir
    r, g, b = [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]
    return f"rgba({r}, {g}, {b}, {opacity})"  # Retorna a string no formato correto

def generate_colorscale(hex_color, color_col):
    min_val, max_val = min(color_col), max(color_col)
    diff = max_val - min_val
    colorscale = []

    if diff > 0:  # Verifica se há valores suficientes para gerar a escala
        step = 1.0 / diff  # Incremento de normalização
        for i in range(diff + 1):
            opacity = i * step
            colorscale.append([opacity, hex_to_rgb(hex_color, opacity)])
    else:
        # Caso haja apenas um valor, usa a cor base
        colorscale = [[0.0, hex_to_rgb(hex_color, 1.0)], [1.0, hex_to_rgb(hex_color, 1.0)]]

    return colorscale


def plot_with_matplotlib(axis_x, axis_y, df_GCA, width_pixels, height_pixels, hover_names):
    # Convert pixels to inches (assuming a standard resolution of 100 dpi)
    width_inches = width_pixels / 100.0
    height_inches = height_pixels / 100.0
    
    # Data preparation
    log_x = np.log(df_GCA[axis_x]);    log_y = np.log(df_GCA[axis_y])
    
    # Plotting the graph
    fig, ax = plt.subplots(figsize=(width_inches, height_inches))
    ax.scatter(df_GCA[axis_x], df_GCA[axis_y], c='blue', alpha=0.5, label='Data Points')
    
    # Fitting a log-log trendline
    model = sm.OLS(log_y, sm.add_constant(log_x)).fit()
    predicted = model.predict(sm.add_constant(log_x))
    ax.plot(df_GCA[axis_x], np.exp(predicted), color='black', label="OLS Fit")
    ax.set_xscale('log');     ax.set_yscale('log')
    ax.set_xlabel(axis_x);    ax.set_ylabel(axis_y)

    pixel_positions = []
    for i in range(len(df_GCA)):
        x, y = df_GCA[axis_x].iloc[i], df_GCA[axis_y].iloc[i]
        pixel_coords = ax.transData.transform((x, y))
        pixel_positions.append(pixel_coords.round(2))
    
    # Generate hover_texts
    hover_texts = [f"original_index: {idx}<br>{name}<br>Pixel: ({int(pixel[0])}, {int(pixel[1])})"
                   for idx, name, pixel in zip(df_GCA['original_index'], hover_names, pixel_positions)]

    plt.close(fig)  # close the figure without showing it
    return pixel_positions, hover_texts

def create_gravity_clustering_graph(Cut_Rad, connected_nodes, total_nodes):
    G = nx.Graph()
    for i in range(total_nodes):
        G.add_node(i)
    for i, nodes in enumerate(connected_nodes):
        for j in nodes:
            G.add_edge(i, j)
    return G

def calculate_graph_and_metrics(Cut_Rad, axis_x, axis_y, index, hover_names, file_name, colorscale_HEX):
    df_GCA = pd.DataFrame({'x': axis_x, 'y': axis_y, 'original_index': index, 'Hovername': hover_names})
    # Calculating pixel positions using matplotlib to obtain positions
    pixel_positions, hover_texts = plot_with_matplotlib('x', 'y', df_GCA, 800, 500, hover_names)
    
    # Base on Gravitional Clustering Algorithm
    def gravity_cluster(Cut_Rad, pixel_positions, index):
        Cut_Rad_Pixel_x_Pixel = []
        for i in range(len(pixel_positions)):
            connected_nodes = [j for j in range(len(pixel_positions)) if i != j 
                               and np.sqrt((pixel_positions[j][0] - pixel_positions[i][0]) ** 2 + 
                                           (pixel_positions[j][1] - pixel_positions[i][1]) ** 2) <= Cut_Rad]
            Cut_Rad_Pixel_x_Pixel.append([index[i], connected_nodes])
        return Cut_Rad_Pixel_x_Pixel

    def get_degree_for_all_nodes(G, total_nodes):
        degree_dict = dict(G.degree())
        degrees = [degree_dict.get(i, 0) for i in range(total_nodes)]
        return degrees

    Cut_Rad = gravity_cluster(Cut_Rad, pixel_positions, df_GCA['original_index'].values)
    G = create_gravity_clustering_graph(Cut_Rad, [nodes for _, nodes in Cut_Rad], len(df_GCA))
    degrees = get_degree_for_all_nodes(G, len(df_GCA))
    
    # Create DataFrame with pixel positions
    df_Pixels = df_GCA.copy()
    df_Pixels['Pixel_Positions'] = pixel_positions
    df_Pixels['Degree_List'] = [[df_GCA['original_index'].iloc[j] for j in connected_nodes] 
                                for i, connected_nodes in Cut_Rad]
    
    # Add Degree_G and Degree_ext to df_Pixels
    df_Pixels['Degree_G'] = degrees
    df_Pixels['Degree_ext'] = [len(connected_nodes) for _, connected_nodes in Cut_Rad]
    
    
    return G, degrees, df_Pixels


# Function to generate the graph map
def save_graph_GCA_svg(G, hover_names, df_GCA, filename, colorscale_HEX):
    pos = nx.spring_layout(G, seed=42)  # Arbitrary layout
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color="#000000"),
                            hoverinfo="none", mode="lines")

    node_x, node_y = [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_degree = list(dict(G.degree()).values())

    # Custom colors based on "Degree_G"
    colorscale = generate_colorscale(colorscale_HEX, df_GCA['Degree_G'])

    # Hover texts to include all columns of df_GCA
    hover_texts_with_index = [f"Index: {idx}<br>{'<br>'.join([f'{col}: {val}' for col, val in row.items()])}"
                              for idx, row in df_GCA.iterrows()]

    node_trace = go.Scatter(x=node_x, y=node_y, mode="markers", hovertext=hover_texts_with_index,
                            marker=dict(color=df_GCA['Degree_G'], size=8, line_width=1.0,
                                        colorbar=dict(thickness=15, title="Node Degree",
                                                      xanchor="left", titleside="right",
                                                      tickvals=[0, df_GCA['Degree_G'].max()],
                                                      ticktext=[0, int(df_GCA['Degree_G'].max())],
                                                      lenmode='fraction', len=1, outlinewidth=0.5,
                                                      xpad=0),
                                        colorscale=colorscale)
                            )

    # Building Print Graph with "go" library (Plotly)
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(title=f"{filename} Graph based on GCA  |  CutRad=5.svg" , titlefont_size=16,                                      
                                     showlegend=False, hovermode="closest", margin=dict(b=0, l=0, r=0, t=40),                                                                        
                                     plot_bgcolor="white", paper_bgcolor="white", width=800, height=400,                                     
                                     annotations=[dict(text="", showarrow=False, xref="paper", yref="paper")],
                                     xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                     yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    # Check if the number of nodes matches the number of municipalities in df_GCA
    if len(G.nodes()) != len(df_GCA):
        print(f"Number of nodes in the graph: {len(G.nodes())}")
        print(f"Number of municipalities in df_GCA: {len(df_GCA)}")
        print("Number of nodes does not match the number of municipalities.")
        
    # Save as .svg file
    # pio.write_image(fig, f"{filename}_graphGCA.svg")
    st.plotly_chart(fig)


# Function to plot the scatter graph
def save_scattergraph(axis_x, axis_y, df_GCA, width_pixels, height_pixels, hover_texts, file_name, colorscale_HEX):
    # Create a graph
    G = nx.Graph()

    # Add nodes to the graph
    for idx, row in df_GCA.iterrows():
        G.add_node(idx, pos=(row[axis_x], row[axis_y]))

    # Add edges to the graph based on the 'Degree_List' column
    for idx, row in df_GCA.iterrows():
        neighbors = row['Degree_List']
        for neighbor_idx in neighbors:
            G.add_edge(idx, neighbor_idx)

    # Data preparation
    log_x = np.log(df_GCA[axis_x])
    log_y = np.log(df_GCA[axis_y])

    # Fitting a log-log trendline
    model = sm.OLS(log_y, sm.add_constant(log_x)).fit()
    predicted = np.exp(model.predict(sm.add_constant(log_x)))

    # Custom colors based on "Degree_G"
    colorscale = generate_colorscale(colorscale_HEX, df_GCA['Degree_G'])

    # Hover_texts to include all columns of df_GCA
    hover_texts_with_index = [f"Index: {idx}<br>{'<br>'.join([f'{col}: {val}' for col, val in row.items()])}" 
                              for idx, row in df_GCA.iterrows()]

    # Building Print Graph with "go" library (Plotly)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_GCA[axis_x], y=df_GCA[axis_y], mode='markers', hovertext=hover_texts_with_index, 
                             showlegend=False, marker=dict(color=df_GCA['Degree_G'], size=8, line_width=1.0,
                                                           colorbar=dict(thickness=15,title="Node Degree",  
                                                                         xanchor="left",titleside="right",                                                                          
                                                                         tickvals=[0, df_GCA['Degree_G'].max()],
                                                                         ticktext=[0, int(df_GCA['Degree_G'].max())],
                                                                         lenmode='fraction',len=1, outlinewidth=0.5,                                                                         
                                                                         xpad=0),
                                                           colorscale=colorscale)))

    fig.add_trace(go.Scatter(x=df_GCA[axis_x], y=predicted, mode='lines', showlegend=False))

    # Add edges to the plot
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='gray', width=1), showlegend=False))

    fig.update_layout(title=f"{file_name} - Scatter Graph", xaxis_type="log", yaxis_type="log", template="simple_white", 
                      xaxis_title=axis_x, yaxis_title=axis_y, width=width_pixels, height=height_pixels)

    # Save as .svg file
    # pio.write_image(fig, f"{filename}_scattergraph.svg")

# Function to plot the scatter graph
def plot_scattergraph(axis_x, axis_y, df_GCA, width_pixels, height_pixels, hover_texts, file_name, colorscale_HEX):
    # Create a graph
    G = nx.Graph()

    # Add nodes to the graph
    for idx, row in df_GCA.iterrows():
        G.add_node(idx, pos=(row[axis_x], row[axis_y]))

    # Add edges to the graph based on the 'Degree_List' column
    for idx, row in df_GCA.iterrows():
        neighbors = row['Degree_List']
        for neighbor_idx in neighbors:
            G.add_edge(idx, neighbor_idx)

    # Data preparation
    log_x = np.log(df_GCA[axis_x])
    log_y = np.log(df_GCA[axis_y])

    # Fitting a log-log trendline
    model = sm.OLS(log_y, sm.add_constant(log_x)).fit()
    predicted = np.exp(model.predict(sm.add_constant(log_x)))

    # Custom colors based on "Degree_G"
    colorscale = generate_colorscale(colorscale_HEX, df_GCA['Degree_G'])

    # Hover_texts to include all columns of df_GCA
    hover_texts_with_index = [f"Index: {idx}<br>{'<br>'.join([f'{col}: {val}' for col, val in row.items()])}" 
                              for idx, row in df_GCA.iterrows()]

    # Building Print Graph with "go" library (Plotly)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df_GCA[axis_x], y=df_GCA[axis_y], mode='markers', hovertext=hover_texts_with_index, 
                             showlegend=False, marker=dict(color=df_GCA['Degree_G'], size=8, line_width=1.0,
                                                           colorbar=dict(thickness=15,title="Node Degree",  
                                                                         xanchor="left",titleside="right",                                                                          
                                                                         tickvals=[0, df_GCA['Degree_G'].max()],
                                                                         ticktext=[0, int(df_GCA['Degree_G'].max())],
                                                                         lenmode='fraction',len=1, outlinewidth=0.5,                                                                         
                                                                         xpad=0),
                                                           colorscale=colorscale)))

    fig.add_trace(go.Scatter(x=df_GCA[axis_x], y=predicted, mode='lines', showlegend=False))

    # Add edges to the plot
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='gray', width=1), showlegend=False))

    fig.update_layout(title=f"{file_name} - Scatter Graph", xaxis_type="log", yaxis_type="log", template="simple_white", 
                      xaxis_title=axis_x, yaxis_title=axis_y, width=width_pixels, height=height_pixels)

    # Save as .svg file
    # pio.write_image(fig, f"{filename}_scattergraph.svg")
    st.plotly_chart(fig)



#######################################
# Filter Cities / group path proximity
#######################################

def get_top_cities_by_degree(dataframe, N_cities):
    """
    Returns the names (Hovername) of the top N cities with the highest Degree_G.
    """
    top_cities = dataframe.nlargest(N_cities, 'Degree_G')['Hovername']
    return top_cities.tolist()


def get_top_cities_degree_paths(dataframe, N_cities):
    """
    Returns a list containing the indices in 'Degree_List' of the top N cities with the highest Degree_G.
    """
    top_cities = dataframe.nlargest(N_cities, 'Degree_G')['Degree_List']
    return top_cities.tolist()


def get_top_cities_degree_paths_with_hovername(dataframe, N_cities):
    """
    Returns a list of lists containing the names (Hovername) corresponding to
    the values in 'Degree_List' of the top N cities with the highest Degree_G.
    """
    # Get the 'Degree_List' of the top N cities with the highest Degree_G
    paths = get_top_cities_degree_paths(dataframe, N_cities)

    # List to store hovername paths
    hovername_paths = []

    # Iterate over each path and map indices to hovernames
    for path in paths:
        # Ensure path is evaluated as a list of indices
        path = eval(path) if isinstance(path, str) else path  # Evaluate string as list
        hovername_path = []
        for index in path:
            # Find the hovername corresponding to the original_index
            hovername = dataframe.loc[dataframe['original_index'] == index, 'Hovername'].values
            if len(hovername) > 0:
                hovername_path.append(hovername[0])
        hovername_paths.append(hovername_path)
    
    return hovername_paths


def path_list_top_cities(dataframe, N_cities):
    """
    Returns a unique list containing the names (Hovername) of all cities
    connected to the top N cities with the highest Degree_G.
    """
    hovername_paths = get_top_cities_degree_paths_with_hovername(dataframe, N_cities)
    path_list = []
    for lst in hovername_paths:
        path_list.extend(lst)  # Add all hovernames directly to the final list
    return path_list

def plot_scatter_loglog(df, axis_x, axis_y, hovername, fixed_color, hubs, cor_hubs, paths, color_paths):
    dados_copy = df.copy()
    # Criar colunas para diferenciar hubs e paths
    dados_copy['is_hub'] = dados_copy[hovername].apply(lambda cidade: cidade in hubs)
    dados_copy['is_path'] = dados_copy[hovername].apply(lambda cidade: cidade in paths)
    dados_copy['hover_text'] = ( "Cidade: " + dados_copy[hovername] +
                                 "<br>Pop: " + dados_copy[axis_x].astype(str) +
                                 "<br>IDHM: " + dados_copy[axis_y].astype(str) +
                                 "<br>Degree_G: " + dados_copy['Degree_G'].astype(str) +
                                 "<br>Degree_List: " + dados_copy['Degree_List'].astype(str)
    )
    # Separar os pontos para hubs, paths e não-hubs
    hubs_data = dados_copy[dados_copy['is_hub']]
    paths_data = dados_copy[dados_copy['is_path']]
    non_special_data = dados_copy[~dados_copy['is_hub'] & ~dados_copy['is_path']]

    # Criar a figura manualmente (não usar px.scatter para evitar duplicação de hover)
    fig = go.Figure()

    # Adicionar pontos dos não-hubs (default)
    fig.add_trace(go.Scatter(
        x=non_special_data[axis_x],
        y=non_special_data[axis_y],
        mode='markers',
        marker=dict(color=fixed_color, size=7, opacity=0.5),
        text=non_special_data['hover_text'],
        hoverinfo='text',  # Apenas texto personalizado será exibido
        name='Outros'
    ))

    # Adicionar pontos dos paths
    fig.add_trace(go.Scatter(
        x=paths_data[axis_x],
        y=paths_data[axis_y],
        mode='markers',
        marker=dict(color=color_paths, size=7, symbol='circle'),
        text=paths_data['hover_text'],
        hoverinfo='text',  # Apenas texto personalizado será exibido
        name='Paths'
    ))

    # Adicionar pontos dos hubs
    fig.add_trace(go.Scatter(
        x=hubs_data[axis_x],
        y=hubs_data[axis_y],
        mode='markers',
        marker=dict(color=cor_hubs, size=12, symbol='star', 
                    line=dict(color='black', width=2)),
        text=hubs_data['hover_text'],
        hoverinfo='text',  # Apenas texto personalizado será exibido
        name='Hubs'
    ))
    
    # Configurações do layout
    fig.update_layout(
        template="simple_white",
        xaxis=dict(title=axis_x, type='log'),
        yaxis=dict(title=axis_y, type='log'),
        height=500
    )

    st.plotly_chart(fig)

