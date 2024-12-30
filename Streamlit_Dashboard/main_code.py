from libraries import st, pd, os

# Initialize session state for navigation and selected country
if "page" not in st.session_state:
    st.session_state.page = "Main Dashboard"

if "selected_country" not in st.session_state:
    st.session_state.selected_country = "Brazil"

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

# Function to load data
def load_data(file_path):
    base_path = os.path.dirname(os.path.abspath(__file__))  # Script Path 
    file_path = os.path.join(base_path, file_name)
    return pd.read_csv(file_path, sep=',')

# Sidebar: Country Selector
with st.sidebar:
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

#############################################################################

# Fixed top navigation buttons
st.markdown("## Navegação")
col1, col2, col3, col4 = st.columns(4)


with col1:
    if st.button("Visualizar com NormalScatters"):
        set_page("NormalScatters")

with col2:
    if st.button("Visualizar com BinScatters"):
        set_page("BinScatters")

with col3:
    if st.button("Visualizar com ScatterGraph"):
        set_page("ScatterGraph")

with col4:
    if st.button("Analisar DataFrame"):
        set_page("AnalyzeDataFrame")


# Page redirection logic
if st.session_state.page == "Main Dashboard":
    st.title("Main Dashboard")
    st.write("Bem-vindo ao painel principal!")

elif st.session_state.page == "NormalScatters":
    from NormalScatter_code import display_normal_scatters
    display_normal_scatters(df,file_name,st.session_state.selected_country)

elif st.session_state.page == "BinScatters":
    st.title("BinScatters (Em Desenvolvimento)")
    st.write("Esta funcionalidade será implementada em breve.")

elif st.session_state.page == "ScatterGraph":
    st.title("ScatterGraph (Em Desenvolvimento)")
    st.write("Esta funcionalidade será implementada em breve.")

elif st.session_state.page == "AnalyzeDataFrame":
    st.title("Análise de DataFrame (Em Desenvolvimento)")
    st.write("Esta funcionalidade será implementada em breve.")

