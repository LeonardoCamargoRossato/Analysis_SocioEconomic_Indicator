from libraries import *

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
    st.markdown('Econophysics Analysis: [Github Projects](https://github.com/LeonardoCamargoRossato/Papers_Supplementary_Info_SI/tree/main)  \
                      | Papers Thesis:[Github Repository](https://github.com/LeonardoCamargoRossato/Analysis_SocioEconomic_Indicator/tree/main) \
                      |  Plataform Courses: https://institutopensemais.com \
                      |  About Author: [Portfolio](https://institutopensemais.com/saiba-mais-sobre-o-autor/) \
              ')

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

    # Fixed top navigation buttons
    st.markdown("## Analisys with Econophysics Technics")
    col1, col2, col3, col4 = st.columns(4)


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
        st.title("Main Dashboard: Cities Compare")
        from Cities_Compare_code import display_cities_compare
        display_cities_compare(countries)


    elif st.session_state.page == "NormalScatters":
        from NormalScatter_code import display_normal_scatters
        display_normal_scatters(countries)

    elif st.session_state.page == "BinScatters":
        st.title("BinScatters (Em Desenvolvimento)")
        st.write("Esta funcionalidade será implementada em breve.")

    elif st.session_state.page == "ScatterGraph":
        st.title("ScatterGraph (Em Desenvolvimento)")
        st.write("Esta funcionalidade será implementada em breve.")

    elif st.session_state.page == "AnalyzeDataFrame":
        st.title("Análise de DataFrame (Em Desenvolvimento)")
        st.write("Esta funcionalidade será implementada em breve.")


if __name__ == "__main__":
    main()