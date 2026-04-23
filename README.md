📊 Analysis Socio-Economic Indicator

Este repositório contém uma aplicação interativa desenvolvida em Python + Streamlit para análise, comparação e visualização de indicadores socioeconômicos entre cidades, regiões e países.

O projeto foi concebido como uma ferramenta analítica para explorar padrões em dados complexos, com foco em visual analytics, comparações multivariadas e interpretação de indicadores.

🚀 Visão Geral

A aplicação permite:

Comparar indicadores entre cidades e regiões
Explorar relações entre variáveis com diferentes tipos de gráficos
Realizar análises visuais interativas
Navegar entre diferentes módulos de análise
Utilizar dados estruturados em arquivos .csv

O sistema foi desenvolvido com uma arquitetura modular, onde cada tipo de análise possui seu próprio módulo independente.

🧠 Principais Funcionalidades
📍 Comparação entre cidades (Cities Compare)
📈 Scatter plots e variações analíticas
🔵 Binscatter para análise de tendência
📊 Visualizações customizadas com Plotly
🎨 Padronização de cores por regiões e países
⚙️ Sistema modular de funções reutilizáveis
🗂️ Estrutura do Projeto
Analysis_SocioEconomic_Indicator/
│
├── Streamlit_Dashboard/
│   │
│   ├── main_code.py
│   ├── functions.py
│   ├── libraries.py
│   ├── colors_countries_and_regions.py
│   │
│   ├── Binscatter_code.py
│   ├── Cities_Compare_code.py
│   ├── NormalScatter_code.py
│   ├── ScatterGraph_code.py
│   │
│   ├── tabelas_csv/
│   ├── images/
│   ├── __pycache__/
│   └── requirements.txt
│
├── GraphGCA/
├── Master_Thesis_EconoPhysics/
├── NormalScatter/
├── ScatterGraph/
│
└── Outros arquivos auxiliares
📁 Descrição das Pastas e Arquivos
🔹 Streamlit_Dashboard/

É o núcleo principal da aplicação web.

main_code.py

Arquivo principal da aplicação Streamlit.
Responsável por:

Gerenciar a interface
Controlar a navegação entre módulos
Integrar todas as funcionalidades
functions.py

Contém funções auxiliares reutilizáveis, como:

Tratamento de dados
Filtros
Manipulação de DataFrames
libraries.py

Centraliza as importações do projeto, garantindo organização e padronização.

colors_countries_and_regions.py

Define os padrões de cores utilizados para:

Países
Regiões
Grupos de análise

Importante para consistência visual nos gráficos.

📊 Módulos de Análise

Cada arquivo representa um tipo específico de análise:

Binscatter_code.py
Implementa gráficos de binscatter
Usado para identificar tendências médias em dados dispersos
Cities_Compare_code.py
Comparação direta entre cidades
Permite análise relativa de indicadores
NormalScatter_code.py
Scatter plots tradicionais
Visualização direta da relação entre variáveis
ScatterGraph_code.py
Versão mais avançada/customizada de scatter plots
Possivelmente integra múltiplas dimensões ou estilizações
📂 tabelas_csv/

Contém os datasets utilizados no sistema.

Dados estruturados de indicadores socioeconômicos
Base para todas as análises realizadas
🖼️ images/

Armazena imagens utilizadas na interface:

Logos
Elementos visuais
Apoio gráfico ao dashboard
⚙️ __pycache__/

Arquivos gerados automaticamente pelo Python (pode ser ignorado).

📦 requirements.txt

Lista de dependências do projeto.
