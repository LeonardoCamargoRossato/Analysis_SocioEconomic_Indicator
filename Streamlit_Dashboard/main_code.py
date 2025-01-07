from libraries import *
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))
# from layout_design import add_top_menu

def main():
    st.set_page_config(page_title='City Comparison', page_icon="🏙️", layout="wide", initial_sidebar_state='auto', 
                       menu_items={
                            "Get help": "https://institutopensemais.com/formulario-de-contato/",
                            "Report a bug": "https://institutopensemais.com/formulario-de-contato/",
                            "About": "# My Streamlit App \n This is a Dashboard Tools for my thesis at UFRGS.\n\n" \
                                     "Paper Github: [Github Repository](https://github.com/LeonardoCamargoRossato/Analysis_SocioEconomic_Indicator/tree/main) . \n\n" \
                                     "Plataform Courses: https://institutopensemais.com \n\n" \
                                     "More Infos: send a email leo.c.rossato@gmail.com"                                  
                       })
    # st.markdown('Econophysics Analysis: [Github Projects](https://github.com/LeonardoCamargoRossato/Papers_Supplementary_Info_SI/tree/main)  \
    #                   | Papers Thesis:[Github Repository](https://github.com/LeonardoCamargoRossato/Analysis_SocioEconomic_Indicator/tree/main) \
    #                   |  Plataform Courses: https://institutopensemais.com \
    #                   |  About Author: [Portfolio](https://institutopensemais.com/saiba-mais-sobre-o-autor/) \
    #           ')

    st.markdown(
        """
        <style>
        .top-menu {
            background-color: #333;
            padding: 5px;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .top-menu a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: bold;
        }
        .top-menu a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="top-menu">
            <a href="https://github.com/LeonardoCamargoRossato/Analysis_SocioEconomic_Indicator/tree/main" target="_blank">GitHub Projects</a> |
            <a href="https://github.com/LeonardoCamargoRossato/Papers_Supplementary_Info_SI" target="_blank">Papers Thesis</a> |
            <a href="https://institutopensemais.com" target="_blank">Platform Courses</a> |
            <a href="https://institutopensemais.com/saiba-mais-sobre-o-autor/" target="_blank">Portfolio Author</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Inject CSS for custom button styling with responsive width
    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: white;
            color: black;
            font-size: 10px;
            height: 3em;
            width: 100%;
            border-radius: 10px;
            border: 1px solid black;
        }
        div.stButton > button:first-child:focus {
            background-color: orange;
            color: white;
            border-color: orange;
            box-shadow: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # add_top_menu()

    # Initialize session state for navigation and selected country
    if "page" not in st.session_state:
        st.session_state.page = "Main Dashboard"

    # Function to switch between pages
    def set_page(page_name):
        st.session_state.page = page_name

    #############################################################################

    # Country and dataset mapping
    countries = {
        "Brazil": 'tabelas_csv/df_Brazil.csv',
        "USA": 'tabelas_csv/df_USA_Per_County.csv',
        "Peru": 'tabelas_csv/df_Peru.csv',
        "Mexico": 'tabelas_csv/df_Mexico.csv',
        "El Salvador": 'tabelas_csv/df_ElSalvador.csv',
        "Chile": 'tabelas_csv/df_Chile.csv'
    }

    #############################################################################

    # Top navigation buttons
    st.markdown("## Analysis with Econophysics Techniques")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        if st.button("NormalScatters Visualizing"):
            set_page("NormalScatters")

    with col2:
        if st.button("BinScatters Visualizing"):
            set_page("BinScatters")

    with col3:
        if st.button("ScatterGraph Visualizing"):
            set_page("ScatterGraph")

    with col4:
        if st.button("DataFrame Analysis"):
            set_page("AnalyzeDataFrame")

    # Page redirection logic
    if st.session_state.page == "Main Dashboard":
        st.title("Main Dashboard: Comparing Cities, Countries and Macrorregions")
        
        col4, col5, col6 = st.columns([1, 1, 1])    

        # Caminho correto para as imagens
        image_path = "./images/"

        # Primeiro coluna
        with col4:
            st.image(f"{image_path}comparing_cities.png", use_container_width=True)

            if st.button("Comparing Cities"):
                set_page("comparing_cities")

        # Segunda coluna
        with col5:
            st.image(f"{image_path}comparing_countries.png", use_container_width=True)
            if st.button("Comparing Countries"):
                set_page("comparing_countries")

        # Terceira coluna
        with col6:
            st.image(f"{image_path}comparing_macrorregions.png", use_container_width=True)
            if st.button("Comparing Macrorregions"):
                set_page("comparing_macrorregions")


    elif st.session_state.page == "NormalScatters":
        from NormalScatter_code import display_normal_scatters
        display_normal_scatters(countries)

    elif st.session_state.page == "BinScatters":
        from Binscatter_code import display_binscatters  # type: ignore
        display_binscatters(countries)

    elif st.session_state.page == "ScatterGraph":
        from ScatterGraph_code import display_scattergraph # type: ignore
        display_scattergraph(countries)

    elif st.session_state.page == "AnalyzeDataFrame":
        st.title("Analyze DataFrame (Under Development)")
        st.write("This feature will be implemented soon.")
    


    elif st.session_state.page == "comparing_cities":
        from Cities_Compare_code import display_cities_compare
        display_cities_compare(countries)

    elif st.session_state.page == "comparing_countries":
        from Binscatter_code import display_binscatters  # type: ignore
        display_binscatters(countries)

    elif st.session_state.page == "comparing_macrorregions":
        from ScatterGraph_code import display_scattergraph # type: ignore
        display_scattergraph(countries)

    elif st.session_state.page == "AnalyzeDataFrame":
        st.title("Analyze DataFrame (Under Development)")
        st.write("This feature will be implemented soon.")

    # from Cities_Compare_code import display_cities_compare
    # display_cities_compare(countries)

if __name__ == "__main__":
    main()