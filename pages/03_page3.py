'''
import streamlit as st

st.header("Page 3")
x = st.slider("x")
st.write(f"x is {x}")
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

# Divide o dashboard em seções
st.header('Visão Geral dos Produtos')
st.subheader('Dados do CSV')
st.write(data)

st.header('Filtrar por País')
countries = data['origin_country'].unique()
selected_country = st.selectbox('Selecione um país', countries)
filtered_data = data[data['origin_country'] == selected_country]
st.subheader(f'Dados do país selecionado: {selected_country}')
st.write(filtered_data)

st.header('Contagem de Avaliações')
ratings_count = data['rating'].value_counts()
st.bar_chart(ratings_count)

st.header('Preço de Varejo vs. Preço de Desconto')
st.scatter_chart(data[['retail_price', 'discount_price']])

st.header('Produto de Exemplo')
product_url = data.iloc[0]['product_picture']
st.image(product_url, use_column_width=True)

# Personalização de Temas
st.markdown(
    """
    <style>
    .css-1v5f6kn {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0px 0px 5px #888888;
    }
    </style>
    """,
    unsafe_allow_html=True
)