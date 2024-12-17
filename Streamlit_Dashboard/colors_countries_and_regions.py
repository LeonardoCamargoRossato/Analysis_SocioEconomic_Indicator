# Color dictionary by macrorregion in Brazil
brazil_macrorregion_colors = {
    "Centro_oeste": "#1F77B4",
    "Sudeste": "#FF7F0E",
    "Norte": "#2CA02C",
    "Nordeste": "#D62728",
    "Sul": "#9467BD"
}

# Colors for macrorregions of El Salvador
el_salvador_macrorregion_colors = {
    "Zona occidental": "#FF5733",  # Strong orange
    "Zona central": "#33FF57",     # Green
    "Zona oriental": "#3357FF"     # Blue
}

# Colors for macrorregions of Chile
chile_macrorregion_colors = {
    "Zona Central": "#FF33A1",      # Pink
    "Zona Sur": "#33FFF5",          # Light blue
    "Zona Norte Grande": "#595000", # Yellow / green
    "Zona Norte Chico": "#FF8C33",  # Orange
    "Zona Austral": "#A133FF",      # Purple
    "nan": "#D3D3D3"                # Gray for NaN values
}

# Colors for macrorregions of Mexico
mexico_macrorregion_colors = {
    "Center-West": "#FF6347",  # Tomato red
    "Northwest": "#4682B4",    # Steel blue
    "South-Southeast": "#32CD32",  # Lime green
    "Northeast": "#FFD700",    # Gold
    "Center": "#8A2BE2"        # Blue violet
}

# Colors for macrorregions of Peru
peru_macrorregion_colors = {
    "Sierra": "#FF4500",  # Orange red
    "Selva": "#228B22",   # Forest green
    "Costa": "#1E90FF"    # Dodger blue
}

# Colors for macrorregions of the USA
usa_macrorregion_colors = {
    "South": "#FF1493",   # Deep pink
    "West": "#20B2AA",    # Light sea green
    "Northeast": "#FF8C00", # Dark orange
    "nan": "#D3D3D3",      # Gray for NaN values
    "Midwest": "#6A5ACD"   # Medium slate blue
}

# Mapping of countries to their respective color dictionaries
macrorregion_color_map = {
    "Brazil": brazil_macrorregion_colors,
    "El Salvador": el_salvador_macrorregion_colors,
    "Chile": chile_macrorregion_colors,
    "Mexico": mexico_macrorregion_colors,
    "Peru": peru_macrorregion_colors,
    "USA": usa_macrorregion_colors
}

# List of colors for different countries
country_colors = {
    "Brazil": "green",
    "Chile": "blue",
    "Peru": "red",
    "Mexico": "purple",
    "El Salvador": "orange",
    "USA": "brown"
}

brazil_states_colors = {
    'AC': '#02f557', 'AM': '#667300', 'AP': '#39b504', 'PA': '#d5e386', 'RO': '#24917a', 'RR': '#62f0ab', 'TO': '#b3ff00',
    'AL': '#ff877a', 'BA': '#ff0000', 'CE': '#ffc7ab', 'MA': '#6e0c02', 'PB': '#a67e6a', 'PE': '#2e0002', 'PI': '#f0719f',
    'RN': '#9e5169', 'SE': '#cf0e4b',
    'ES': '#fad264', 'MG': '#a13300', 'RJ': '#807058', 'SP': '#faa764',
    'GO': '#bae3ff', 'MS': '#0097ff', 'MT': '#00087d',
    'PR': '#dec9ff', 'RS': '#5e347d', 'SC': '#ff7abf'
}

usa_states_colors = {
    'AL': '#ff0000', 'AK': '#00ff00', 'AZ': '#0000ff', 'AR': '#ffff00', 'CA': '#ff00ff', 'CO': '#00ffff',
    'CT': '#800000', 'DE': '#808000', 'DC': '#008000', 'FL': '#800080', 'GA': '#808080', 'HI': '#c0c0c0',
    'ID': '#ff8080', 'IL': '#80ff80', 'IN': '#8080ff', 'IA': '#ffff80', 'KS': '#ff80ff', 'KY': '#80ffff',
    'LA': '#ffcc00', 'ME': '#ff6666', 'MD': '#66ff66', 'MA': '#6666ff', 'MI': '#cccc00', 'MN': '#cc00cc',
    'MS': '#00cccc', 'MO': '#cc6666', 'MT': '#66cc66', 'NE': '#6666cc', 'NV': '#99cc99', 'NH': '#cc9999',
    'NJ': '#9999cc', 'NM': '#cc99cc', 'NY': '#99cc99', 'NC': '#cc9966', 'ND': '#669999', 'OH': '#996699',
    'OK': '#999966', 'OR': '#669966', 'PA': '#666699', 'RI': '#996666', 'SC': '#99cccc', 'SD': '#6699cc',
    'TN': '#9966cc', 'TX': '#cccc66', 'UT': '#66cccc', 'VT': '#cc6666', 'VA': '#99ff99', 'WA': '#ff9999',
    'WV': '#66cc99', 'WI': '#99ccff', 'WY': '#ccff99'
}

mexico_states_colors = {
    'Aguascalientes': '#ff0000', 'Baja California': '#00ff00', 'Baja California Sur': '#0000ff',
    'Campeche': '#ffff00', 'Coahuila': '#ff00ff', 'Colima': '#00ffff', 'Chiapas': '#800000',
    'Chihuahua': '#808000', 'Distrito Federal': '#008000', 'Durango': '#800080', 'Guanajuato': '#808080',
    'Jalisco': '#c0c0c0', 'México': '#ff8080', 'Michoacán': '#80ff80', 'Morelos': '#8080ff',
    'Nayarit': '#ffff80', 'Nuevo León': '#ff80ff', 'Oaxaca': '#80ffff', 'Puebla': '#ffcc00',
    'Querétaro': '#ff6666', 'Quintana Roo': '#66ff66', 'San Luis Potosí': '#6666ff', 'Sonora': '#cccc00',
    'Tabasco': '#cc00cc', 'Tamaulipas': '#00cccc', 'Tlaxcala': '#cc6666', 'Veracruz': '#66cc66',
    'Yucatán': '#6666cc', 'Zacatecas': '#99cc99'
}

peru_states_colors = {
    'AMAZONAS': '#ff0000', 'ANCASH': '#00ff00', 'APURÍMAC': '#0000ff', 'AREQUIPA': '#ffff00',
    'AYACUCHO': '#ff00ff', 'CAJAMARCA': '#00ffff', 'CUSCO': '#800000', 'HUANCAVELICA': '#808000',
    'HUÁNUCO': '#008000', 'ICA': '#800080', 'JUNÍN': '#808080', 'LA LIBERTAD': '#c0c0c0',
    'LAMBAYEQUE': '#ff8080', 'LIMA': '#80ff80', 'LORETO': '#8080ff', 'MADRE DE DIOS': '#ffff80',
    'MOQUEGUA': '#ff80ff', 'PASCO': '#80ffff', 'PIURA': '#ffcc00', 'PUNO': '#ff6666',
    'SAN MARTÍN': '#66ff66', 'TACNA': '#6666ff', 'TUMBES': '#cccc00', 'UCAYALI': '#cc00cc'
}

elsalvador_states_colors = {
    'Ahuachapán': '#ff0000', 'Cabañas': '#00ff00', 'Chalatenango': '#0000ff',
    'Cuscatlán': '#ffff00', 'La Libertad': '#ff00ff', 'La Paz': '#00ffff',
    'La Unión': '#800000', 'Morazán': '#808000', 'San Miguel': '#008000',
    'San Salvador': '#800080', 'San Vicente': '#808080', 'Santa Ana': '#c0c0c0',
    'Sonsonate': '#ff8080', 'Usulután': '#80ff80'
}

chile_regions_colors = {
    'VALPARAÍSO': '#ff0000', 'RM': '#00ff00', 'BIOBÍO': '#0000ff',
    'TARAPACÁ': '#ffff00', 'LOS LAGOS': '#ff00ff', 'COQUIMBO': '#00ffff',
    'ARAUCANÍA': '#800000', 'ANTOFAGASTA': '#808000', 'ARICA Y PARINACOTA': '#008000',
    'AYSÉN': '#800080', 'BIOBÍO-ÑUBLE': '#808080', 'MAGALLANES': '#c0c0c0',
    'ATACAMA': '#ff8080', 'MAULE': '#80ff80', "O'HIGGINS": '#8080ff',
    'LOS RÍOS': '#ffff80', 'LOS RIOS': '#ff80ff'
}

state_color_mapping_countries = {
    'Brazil': brazil_states_colors,
    'USA': usa_states_colors,
    'Mexico': mexico_states_colors,
    'Peru': peru_states_colors,
    'Chile': chile_regions_colors,
    'ElSalvador': elsalvador_states_colors
}
