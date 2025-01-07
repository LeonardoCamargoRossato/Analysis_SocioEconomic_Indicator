from libraries import *
from functions import *
from colors_countries_and_regions import *

# Function to load data
def load_data(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))  # Script Path 
    file_path = os.path.join(base_path, file_name)
    return pd.read_csv(file_path, sep=',')

def display_scattergraph(countries):

    if "selected_country" not in st.session_state:
        st.session_state.selected_country = "Brazil"

    country_color = country_colors[st.session_state.selected_country]
    st.markdown(
        "<h4 style='text-align: left; color: white;'>Analysis Options</h4>",
        unsafe_allow_html=True
    )
    st.markdown("Caution: ScatterGraph and BGCA with Country Brazil, USA and Big Macrorregions "
                "usually take longer between 1min-5min to be loaded / plotted.")

    with st.sidebar:
        # Styling for full-width buttons
        st.markdown("""
            <style>
            .full-width-button {
                width: 100% !important;
                height: 30px;
                font-size: 14px;
            }
            </style>
                    
        """, unsafe_allow_html=True)
        # "Back to Main Dashboard" button
        if st.button("Back to Main Dashboard", key="back_to_main_dashboard", help="Return to the Main Dashboard", use_container_width=True):
            st.session_state.page = "Main Dashboard"


        selected_country = st.selectbox(
            "Select Country",
            options=list(countries.keys()),
            index=list(countries.keys()).index(st.session_state.selected_country),
            key="country_selector"
        )
        st.session_state.selected_country = selected_country

        # Load the selected country's data
        file_name = countries[st.session_state.selected_country]
        df = load_data(file_name)

        # Logic for viewing the DataFrame
        if "show_dataframe" not in st.session_state:
            st.session_state.show_dataframe = False

        # Dynamic DataFrame Viewing Button
        if st.session_state.show_dataframe:
            if st.button("Hide DataFrame", key="hide_df", help="Hide the DataFrame", use_container_width=True):
                st.session_state.show_dataframe = False
        else:
            if st.button("Show DataFrame", key="show_df", help="Display the DataFrame", use_container_width=True):
                st.session_state.show_dataframe = True

        st.markdown(f"**Data File:** `{file_name}`")


        country = st.session_state.selected_country
        if country == 'Brazil':
            index_axis_x = 'Total_Pop_Absol'; index_axis_y = 'IDHM_2010'
            index_color_column = 'Macroregioes'; index_hovername = 'Municipio'
        elif country == 'USA':
            index_axis_x = '2015_Tract_population'; index_axis_y = 'unadjusted_hdi'
            index_color_column = 'Macroregion'; index_hovername = 'County_States'
        elif country == 'Peru':
            index_axis_x = 'Pop_2017'; index_axis_y = 'HDI_2017'
            index_color_column = 'Macroregioes_Topografica'; index_hovername = 'City'
        elif country == 'Mexico':
            index_axis_x = 'Pop_Total_2010'; index_axis_y = 'IDH_2000'
            index_color_column = 'Macroregioes'; index_hovername = 'Hovername'
        elif country == 'El Salvador':
            index_axis_x = 'Pop_total_2005'; index_axis_y = 'IDH_2005'
            index_color_column = 'Macroregioes'; index_hovername = 'Comuna'
        elif country == 'Chile':
            index_axis_x = 'Población_2017'; index_axis_y = 'IDC_2020'
            index_color_column = 'Macroregioes'; index_hovername = 'COMUNA'            
        else:
            index_axis_x = None; index_axis_y = None
            index_color_column = None; index_hovername = None       



        st.header("Settings")
        axis_x = st.selectbox("Select X-axis", options=df.columns, index=list(df.columns).index(index_axis_x))
        axis_y = st.selectbox("Select Y-axis", options=df.columns, index=list(df.columns).index(index_axis_y))
        color_column = st.selectbox("Select Color Column", options=list(df.columns), index=list(df.columns).index(index_color_column))
        hovername = st.selectbox("Select Hovername Column", options=list(df.columns), index=list(df.columns).index(index_hovername))

    # Display the DataFrame on the main screen
    if st.session_state.show_dataframe:
        st.subheader("DataFrame Row Control")
        col1, col2 = st.columns(2)

        with col1:
            min_row = st.number_input("Start Row", min_value=0, max_value=len(df)-1, value=0, step=1)
        with col2:
            max_row = st.number_input("End Row", min_value=1, max_value=len(df), value=10, step=1)

        # Ensure start row is not greater than end row
        if min_row > max_row:
            st.warning("The start row cannot be greater than the end row.")
        else:
            st.subheader(f"Displaying Rows {min_row} to {max_row}")
            st.dataframe(df.iloc[min_row:max_row])



 #################################################################################################################
    # Per Country, Per Macrorregion, Per States
 #################################################################################################################

    # Initialize session state for region mode if not set
    if "region_mode" not in st.session_state:
        st.session_state.region_mode = "Per Country"

    # Row of buttons for display mode with dynamic styles
    # st.markdown("<hr style='border: 0.1 px solid white;'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Per Country", key="per_country", help="Analyze per country"):
            st.session_state.region_mode = "Per Country"

    with col2:
        if st.button("Per Macrorregion", key="per_macrorregion", help="Analyze per macrorregion"):
            st.session_state.region_mode = "Per Macrorregion"

    with col3:
        if st.button("Per Regions / States", key="per_regions_states", help="Analyze per region or state"):
            st.session_state.region_mode = "Per Regions / States"

    # Conditional logic for selected region
    if st.session_state.region_mode == "Per Country":
        df_selected = df
        specific_color = select_color_country(country)
    elif st.session_state.region_mode == "Per Macrorregion":
        macrorregion = country_macrorregions_list(df, country)
        select_macrorregion = st.selectbox("Select Macrorregion", macrorregion[0])
        df_selected = df[df[macrorregion[1]] == str(select_macrorregion)]  # Fixed
        specific_color = select_color_one_macrorregion_country(country, select_macrorregion)
    elif st.session_state.region_mode == "Per Regions / States":
        state = country_states_list(df, country)
        select_state = st.selectbox("Select State", state[0])
        df_selected = df[df[state[1]] == str(select_state)]  # Fixed
        specific_color = select_color_one_state_country(country, select_state)


    # Add spacing and horizontal line
    # st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 0.01 px solid white;'>", unsafe_allow_html=True)

    # Visualization Options with dynamic button styles
    st.markdown("<h4 style='text-align: center;'>Visualization Options:</h4>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)

    # Initialize session state for visualization mode if not set
    if "visualization_mode" not in st.session_state:
        st.session_state.visualization_mode = "Plot Scatter"

    with col4:
        if st.button("ScatterGraph", key="plot_scattergraph"):
            st.session_state.visualization_mode = "Plot ScatterGraph"

    with col5:
        if st.button("BGCA (Graph)", key="plot_BGCA_graph"):
            st.session_state.visualization_mode = "Plot BGCA graph"

    with col6:
        if st.button("NormalScatter", key="plot_scattergraph_colors"):
            st.session_state.visualization_mode = "Plot ScatterGraph Colors"



    # Render the selected plot based on the active mode
    fig = None
    if st.session_state.visualization_mode == "Plot ScatterGraph":
        Cut_Rad = st.slider("Select Cut Radius Circle (Arbitrary Value)", min_value=1, max_value=100, value=5, step=1)
        colorscale_HEX = specific_color; filename = country
        G, degree, df_Pixels = calculate_graph_and_metrics(Cut_Rad, df_selected[axis_x], df_selected[axis_y], df_selected.index, hovername, filename, colorscale_HEX)
        # save_graph_GCA_svg(G, hovername, df_Pixels, filename, colorscale_HEX)
        plot_scattergraph('x', 'y', df_Pixels, 800, 500, df_Pixels['Hovername'], filename, colorscale_HEX)

    elif st.session_state.visualization_mode == "Plot BGCA graph":
        Cut_Rad = st.slider("Select Cut Radius Circle (Arbitrary Value)", min_value=1, max_value=100, value=5, step=1)
        colorscale_HEX = specific_color; filename = country
        G, degree, df_Pixels = calculate_graph_and_metrics(Cut_Rad, df_selected[axis_x], df_selected[axis_y], df_selected.index, hovername, filename, colorscale_HEX)
        save_graph_GCA_svg(G, hovername, df_Pixels, filename, colorscale_HEX)

    elif st.session_state.visualization_mode == "Plot ScatterGraph Colors":
        fig = Plot_Scatter_No_Trendline(df_selected, axis_x, axis_y, hovername, specific_color)


    if fig:
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr style='border: 0.1 px solid white;'>", unsafe_allow_html=True)

    fixed_color = '#5e347d'  # Cor padrão para os pontos
    hubs =  get_top_cities_by_degree(df_selected, 5)
    cor_hubs = '#f59542'  # Cor para as cidades na lista de hubs
    paths = path_list_top_cities(df_selected, 5)[0]
    color_paths = '#f59542'  # Cor para as cidades na lista de paths
    plot_scatter_loglog(df_selected, axis_x, axis_y, hovername, fixed_color, hubs, cor_hubs, paths, color_paths)