'''
import streamlit as st

st.header("Page 5")
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

# Botão para limpar todos os filtros
if st.button('Limpar Filtros'):
    filtered_data = data
    min_rating, selected_color, selected_shipping_option, min_inventory = 0.0, None, None, 0


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

# Gráfico de pizza para mostrar as porcentagens de cores dos produtos
st.header('Porcentagens de Cores dos Produtos')
color_percentage = filtered_data['product_color'].value_counts() / len(filtered_data) * 100

# Configurações de estilo para o gráfico de pizza
fig, ax = plt.subplots()
ax.pie(color_percentage, labels=color_percentage.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'))
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Exibir o gráfico usando st.pyplot()
st.pyplot(fig)
