import streamlit as st
import pandas as pd
st.header("Page 2")



# Carrega os dados do arquivo CSV
@st.cache  # Cache para melhor desempenho
def load_data():
    data = pd.read_csv('2020.csv')
    return data

data = load_data()

# Título do aplicativo
st.title('Dashboard de Produtos')

# Exibir os dados em uma tabela
st.subheader('Dados do CSV')
st.write(data)
#st.write(data.columns)

# Opção para filtrar os dados por país
countries = data['origin_country'].unique()
selected_country = st.selectbox('Filtrar por País', countries)
filtered_data = data[data['origin_country'] == selected_country]

# Exibir os dados filtrados em uma tabela
st.subheader(f'Dados do país selecionado: {selected_country}')
st.write(filtered_data)

# Gráfico de barras para contagem de avaliações
st.subheader('Contagem de Avaliações')
ratings_count = data['rating'].value_counts()
st.bar_chart(ratings_count)

# Gráfico de dispersão para preço de varejo vs. preço de desconto
st.subheader('Preço de Varejo vs. Preço de Desconto')
st.scatter_chart(data[['retail_price', 'discount_price']])

# Exibir uma imagem de um produto de exemplo
st.subheader('Produto de Exemplo')
product_url = data.iloc[0]['product_picture']
st.image(product_url, use_column_width=True)

# Rodapé
st.footer('Desenvolvido com Streamlit')