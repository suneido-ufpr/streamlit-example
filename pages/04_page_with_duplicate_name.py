'''
import streamlit as st

st.header("Page 4")
'''


import streamlit as st
import pandas as pd

# Carrega os dados do arquivo CSV
@st.cache
def load_data():
    data = pd.read_csv('2020.csv')
    return data

data = load_data()

# Define o título do aplicativo e o estilo do título
st.title('Dashboard de Produtos')
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Filtros
st.header('Filtros')
col1, col2, col3, col4 = st.beta_columns(4)

# Filtro por Classificação
with col1:
    min_rating = st.slider('Classificação Mínima', min_value=0, max_value=5, step=0.1, value=0)
    filtered_data = data[data['rating'] >= min_rating]

# Filtro por Cor do Produto
with col2:
    selected_color = st.selectbox('Cor do Produto', data['product_color'].unique())
    filtered_data = filtered_data[filtered_data['product_color'] == selected_color]

# Filtro por Opção de Envio
with col3:
    selected_shipping_option = st.selectbox('Opção de Envio', data['shipping_option_name'].unique())
    filtered_data = filtered_data[filtered_data['shipping_option_name'] == selected_shipping_option]

# Filtro por Total de Inventário
with col4:
    min_inventory = st.slider('Inventário Mínimo', min_value=0, max_value=data['inventory_total'].max(), value=0)
    filtered_data = filtered_data[filtered_data['inventory_total'] >= min_inventory]

st.header('Produtos Filtrados')
st.write(filtered_data)
