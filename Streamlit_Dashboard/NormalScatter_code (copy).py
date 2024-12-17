from libraries import st
from functions import *
from colors_countries_and_regions import *

def display_normal_scatters(df, file_name, country):

    country_color = select_color_country(country)

    st.markdown(
        "<h2 style='text-align: Left; color: white;'>Analysis per Country: all macrorregions </h1>",
        unsafe_allow_html=True
    )

    with st.sidebar:
        # Estilização para largura total do botão
        st.markdown("""
            <style>
            .full-width-button {
                width: 100% !important;
                height: 50px; /* Altura opcional */
                font-size: 16px; /* Tamanho do texto opcional */
            }
            </style>
        """, unsafe_allow_html=True)

        # Botão "Voltar ao Dashboard Principal"
        if st.button("Voltar ao Dashboard Principal", key="voltar_dashboard_normal_scatter", help="Retornar ao Dashboard Principal", use_container_width=True):
            st.session_state.page = "Dashboard Principal"

        # Logic for viewing the DataFrame
        if "show_dataframe" not in st.session_state:
            st.session_state.show_dataframe = False

        # Dynamic DataFrame Viewing Button
        if st.session_state.show_dataframe:
            if st.button("Parar de ver DataFrame", key="stop_view_df", help="Parar de exibir o DataFrame", use_container_width=True):
                st.session_state.show_dataframe = False
        else:
            if st.button("Ver DataFrame", key="view_df", help="Exibir o DataFrame", use_container_width=True):
                st.session_state.show_dataframe = True

        st.markdown(f"**Arquivo de Dados:** `{file_name}`")


        st.header("Configurações")
        axis_x = st.selectbox("Selecione o eixo X", options=df.columns)
        axis_y = st.selectbox("Selecione o eixo Y", options=df.columns)
        color_column = st.selectbox("Selecione a coluna para cor", options=[None] + list(df.columns))
        hovername = st.selectbox("Selecione a coluna para Hovername", options=list(df.columns))


    # Exibição do DataFrame na tela principal
    if st.session_state.show_dataframe:
        st.subheader("Controle de Linhas do DataFrame")
        col1, col2 = st.columns(2)

        with col1:
            min_row = st.number_input("Linha Inicial", min_value=0, max_value=len(df)-1, value=0, step=1)
        with col2:
            max_row = st.number_input("Linha Final", min_value=1, max_value=len(df), value=10, step=1)

        # Garantir que a linha inicial não seja maior que a linha final
        if min_row > max_row:
            st.warning("A linha inicial não pode ser maior que a linha final.")
        else:
            st.subheader(f"Exibindo Linhas {min_row} a {max_row}")
            st.dataframe(df.iloc[min_row:max_row])

    # Organizar os botões em uma única linha com colunas
    col1, col2, col3, col4 = st.columns(4)
    fig = None

    # Estilização para botões
    st.markdown("""
        <style>
        .stButton > button {
            width: 150px; /* Largura fixa para os botões */
            height: 50px; /* Altura fixa para os botões */
            margin: 0 auto; /* Centraliza os botões */
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stButton {
            padding: 5px; /* Adiciona espaçamento entre os botões */
        }
        </style>
    """, unsafe_allow_html=True)

    # Botão para Plot_Scatter
    with col1:
        if st.button("Plotar Scatter"):
            fig = Plot_Scatter(df, axis_x, axis_y, color_column,hovername)

    # Botão para Plot_Scatter_No_Regions
    with col2:
        if st.button("Scatter sem Regiões"):
            fig = Plot_Scatter_No_Regions(df, axis_x, axis_y,hovername, country_color)

    # Botão para Plot_Scatter_No_Trendline
    with col3:
        if st.button("Scatter sem Trendline"):
            fig = Plot_Scatter_No_Trendline(df, axis_x, axis_y,hovername, country_color)

    # Botão para Plot_Scatter_Simple
    with col4:
        if st.button("Scatter Simples"):
            fig = Plot_Scatter_Simple(df, axis_x, axis_y,hovername, country_color)

    # Renderizando o gráfico abaixo dos botões, ocupando toda a largura
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)

#################################################################################################################
#  Per Macrorregion | Per States
#################################################################################################################

    st.markdown(
        "<h2 style='text-align: Left; color: white;'>Analysis More Deep: per Macrorregions or per States </h1>",
        unsafe_allow_html=True
    )


    # Estado inicial dos botões
    if "region_mode" not in st.session_state:
        st.session_state.region_mode = "Per Macrorregion"  

    # Linha de botões para modo de exibição
    st.markdown("<h4 style='text-align: center;'>Select Display Mode:</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Per Macrorregion", key="per_macrorregion"):
            st.session_state.region_mode = "Per Macrorregion"

    with col2:
        if st.button("Per Regions / States", key="per_regions_states"):
            st.session_state.region_mode = "Per Regions / States"

    
    # Exibição condicional com base no botão selecionado
    if st.session_state.region_mode == "Per Macrorregion":
        macrorregion = country_macrorregions_list(df,country)
        select_macrorregion = st.selectbox("Select Macrorregion", macrorregion[0])
        df_macroregions_states = df[df[macrorregion[1]] == str(select_macrorregion)]
        specific_color = select_color_one_macrorregion_country(country, select_macrorregion)

    elif st.session_state.region_mode == "Per Regions / States":
        state = country_states_list(df,country)
        select_state = st.selectbox("Select State", state[0])
        df_macroregions_states = df[df[state[1]] == str(select_state)]
        specific_color = select_color_one_state_country(country, select_state)
  
    # Espaçamento entre os botões e as opções de plotagem
    st.markdown("<br>", unsafe_allow_html=True)

    # Linha de botões para plotagem
    st.markdown("<h4 style='text-align: center;'>Visualization Options:</h4>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    fig = None

    with col1:
        if st.button("Plotar Scatter", key="plotar_scatter_normal"):
            fig = Plot_Scatter(df_macroregions_states, axis_x, axis_y, color_column, hovername)

    with col2:
        if st.button("Scatter sem Regiões", key="scatter_sem_regioes"):
            fig = Plot_Scatter_No_Regions(df_macroregions_states, axis_x, axis_y, hovername, specific_color)

    with col3:
        if st.button("Scatter sem Trendline", key="scatter_sem_trendline"):
            fig = Plot_Scatter_No_Trendline(df_macroregions_states, axis_x, axis_y, hovername, specific_color)


    with col4:
        if st.button("Scatter Simples", key="scatter_simples"):
            fig = Plot_Scatter_Simple(df_macroregions_states, axis_x, axis_y, hovername, specific_color)

    # Renderizando o gráfico abaixo dos botões, ocupando toda a largura
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)

