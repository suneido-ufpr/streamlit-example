'''
import streamlit as st

st.header("Page 4")
'''


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Divide o espaço horizontal em quatro colunas
col1, col2, col3, col4 = st.columns(4)

# Filtro por Classificação
with col1:
    min_rating = st.slider('Classificação Mínima', min_value=0.0, max_value=5.0, step=0.1, value=0.0)
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
    min_inventory = st.slider('Inventário Mínimo', min_value=0, max_value=int(data['inventory_total'].max()), value=0)
    filtered_data = filtered_data[filtered_data['inventory_total'] >= min_inventory]

st.header('Produtos Filtrados')
st.write(filtered_data)

# Gráfico de barras para mostrar as porcentagens de cores dos produtos
st.header('Porcentagens de Cores dos Produtos')
color_percentage = filtered_data['product_color'].value_counts() / len(filtered_data) * 100

# Configurações de estilo para o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=color_percentage.index, y=color_percentage.values, palette='viridis', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_xlabel('Cor do Produto')
ax.set_ylabel('Porcentagem')
ax.set_title('Porcentagens de Cores dos Produtos')

# Exibir o gráfico usando st.pyplot()
st.pyplot(fig)









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

# Divide o espaço horizontal em quatro colunas
col1, col2, col3, col4 = st.columns(4)

# Filtro por Classificação
with col1:
    min_rating = st.slider('Classificação Mínima', min_value=0.0, max_value=5.0, step=0.1, value=0.0)
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
    min_inventory = st.slider('Inventário Mínimo', min_value=0, max_value=int(data['inventory_total'].max()), value=0)
    filtered_data = filtered_data[filtered_data['inventory_total'] >= min_inventory]

st.header('Produtos Filtrados')
st.write(filtered_data)
'''