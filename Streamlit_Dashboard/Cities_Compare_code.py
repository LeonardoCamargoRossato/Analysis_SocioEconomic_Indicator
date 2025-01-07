from libraries import *
from functions import *
from colors_countries_and_regions import *

def load_data(file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))  # Script Path 
    file_path = os.path.join(base_path, file_name)
    return pd.read_csv(file_path, sep=',')

def display_cities_compare(countries):
    st.write("Choose 2 cities for compare")
    # col1, _, col2 = st.columns([4.5, 1, 4.5])
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### City 1:")

        # Step 1: Select Country
        city1_country = st.selectbox("Select Country", options=list(countries.keys()), key="city1_country")
        color_country = country_colors[city1_country]
        df = load_data(countries[city1_country])
        
        # Step 2: Select State
        city1_dict = get_country_info(city1_country)
        city1_index_axis_x = city1_dict["index_axis_x"]
        city1_index_axis_y = city1_dict['index_axis_y']
        city1_index_state_column = city1_dict['index_state_column']
        city1_index_hovername = city1_dict['index_hovername']

         # Step 3: Select State
        if city1_index_state_column in df.columns:
            states = df[city1_index_state_column].unique()
            city1_state = st.selectbox("Select State", options=states, key="city1_state")
        else:
            city1_state = None

        # Step 4: Select City
        if city1_state:
            cities = df[df[city1_index_state_column] == city1_state][city1_index_hovername].unique()
            city_name = st.selectbox("Select City", options=cities, key="city1_name")
        else:
            city_name = None

        # Plot
        if city_name:
            fig = create_interactive_scatter_go(
                df=df, axis_x=city1_index_axis_x, axis_y=city1_index_axis_y, hovername_city_column=city1_index_hovername, 
                color_city="#ffffff", color_country=color_country, selected_city=city_name
            )
            st.plotly_chart(fig, key="city1_chart", use_container_width=True)

    with col2:
        st.markdown("### City 2:")

        # Similar logic for City 2 with unique keys
        countries_list = list(countries.keys()); default_index = countries_list.index('Peru')
        city2_country = st.selectbox("Select Country", options=list(countries.keys()), key="city2_country", index=default_index)
        color_country2 = country_colors[city2_country]
        df2 = load_data(countries[city2_country])
        
        # Step 2: Select State
        city2_dict = get_country_info(city2_country)
        city2_index_axis_x = city2_dict['index_axis_x']
        city2_index_axis_y = city2_dict['index_axis_y']
        city2_index_state_column = city2_dict['index_state_column']
        city2_index_hovername = city2_dict['index_hovername']

        # Configure parameters for City 2
        if city2_country:
            states2 = df2[city2_index_state_column].unique()
            city2_state = st.selectbox("Select State", options=states2, key="city2_state")
        else:
            city2_state = None

        if city2_state:
            cities2 = df2[df2[city2_index_state_column] == city2_state][city2_index_hovername].unique()
            city2_name = st.selectbox("Select City", options=cities2, key="city2_name")
        else:
            city2_name = None

        # Plot for City 2
        if city2_name:
            fig2 = create_interactive_scatter_go(
                df=df2, axis_x=city2_index_axis_x, axis_y=city2_index_axis_y, hovername_city_column=city2_index_hovername, 
                color_city="#ffffff", color_country=color_country2, selected_city=city2_name
            )
            st.plotly_chart(fig2, key="city2_chart", use_container_width=True)