#Simplesmente executando essa função você irá obter um novo arquivo CSV com os dados aleatórios. Agora, para exibir a tabela basta utilizar a biblioteca Streamlit.

#Execute essa linha após a execução da função generate_data(). Ela irá carregar o novo arquivo CSV e exibi-lo como uma tabela.
#Agora você tem um app completo para realizar todas as etapas solicitadas pelo usuário.


import streamlit as st

import pandas as pd

from faker import Faker

fake = Faker()
import random
import string
import re
import numpy as np
import math
import time
import csv

#Função para ler o arquivo CSV
def read_file(filename):
    df = pd.read_csv(filename)
    return df
#Função para gerar dados aleatórios baseados nos padrões encontrados
def generate_data():
    # Leitura do arquivo CSV
    data = read_file("RefundProcess.csv")
    
    # Identificação dos padrões presentes nas colunas
    status_patterns = []
    employee_patterns = []
    complete_timestamp_patterns = []
    channel_patterns = []
    
    for column in data.columns:
        if column == 'Order Nr.':
            continue
        pattern = r''.join([random.choice(['[A-Z]'] + [random.choice(string.digits)] * (len(column)-1)) for _ in range(10)])
        regexp = re.compile('^'+pattern+'$')
        matches = list(filter(regexp.match, data['Order Nr.'].unique()))
        status_patterns.append((column, pattern, len(matches)))
        pattern = r'\w+'
        regexp = re.compile('^'+pattern+'$')
        matches = list(set(list(filter(regexp.match, data[column].unique())).difference({np.nan})))
        employee_patterns.append((column, pattern, len(matches), matches))
    
        pattern = r'\d{2}/\d{2}/\d{2}\s+\d{2}:\d{2}'
        regexp = re.compile('^'+pattern+'$')
        matches = list(set(list(filter(regexp.match, data[column].unique())).difference({np.nan}))[:math.ceil(len(data)/10)])
        complete_timestamp_patterns.append((column, pattern, len(matches), matches))
    
        pattern = r'\w+'
        regexp = re.compile('^'+pattern+'$')
        matches = list(set(list(filter(regexp.match, data[column].unique())).difference({np.nan}))[:math.ceil(len(data)/10)])
        channel_patterns.append((column, pattern, len(matches), matches))
    
    print(status_patterns)
    print(employee_patterns)
    print(complete_timestamp_patterns)
    print(channel_patterns)
    
    # Geração de dados aleatórios
    new_rows = []
    for i in range(1000):
        row = {}
        for column, pattern, count, choices in status_patterns:
            row[column] = fake.lexify(text=pattern)
    
        for column, pattern, count, choices in employee_patterns:
            row[column] = random.sample(choices, k=1)[0]
    
        for column, pattern, count, choices in complete_timestamp_patterns:
            row[column] = fake.date("%m/%d/%Y %H:%M", pattern="%m/%d/%y %H:%M")
    
        for column, pattern, count, choices in channel_patterns:
            row[column] = random.sample(choices, k=1)[0]
    
        new_rows.append(row)
    
    # Criação de um DataFrame com os dados aleatórios
    new_df = pd.DataFrame(new_rows)
    
    # Adição dos dados ao dataframe original
    result = pd.concat([data, new_df], ignore_index=True)
    
    # Escrita do novo dataframe em um arquivo CSV
    timestamp = int(time.time())
    filename = f"RefundProcess_{str(timestamp)}.csv"
    result.to_csv(filename, index=False)
    
    return filename

#Executando a função
generate_data()

st.table(pd.read_csv("RefundProcess_" + str(timestamp) + ".csv"))


'''import streamlit as st

st.header("Main Page")
st.slider("x")
'''


'''
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

#st.session_state.key = 'home'

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# This is a header. This is an *extremely* cool app!"
    }
)

def my_new_page_write():
    st.write("This is my new page!")

def home_write():
    st.write("This is the home page!")

st.title('my_new_page x')

if 'my_new_page' not in st.session_state:
    st.session_state.my_new_page = my_new_page_write

if 'home' not in st.session_state:
    st.session_state.home = home_write

st.sidebar.button("streamlit app", on_click=st.session_state.home)
st.sidebar.button("my new page", on_click=st.session_state.my_new_page)


st.session_state.my_new_page = lambda: st.write("This is my new page!")
st.session_state.home = lambda: st.write("This is the home page!")
'''


# st.help(st.sidebar.selectbox)

# st.sidebar.button("my new page", on_click=st.session_state.set, args=["my_new_page"])
# if st.session_state.get("page") == "my_new_page":
#     st.write("xxxxxxxxxxxxxxxxxxxxxxxxx")

#if st.sidebar.selectbox("streamlit app", True):
#    st.write("streamlit app")
#else:
#    st.write("NOO streamlit app")
#
#if st.sidebar.selectbox('my new page', True):
#    st.write("my new page")


#st.sidebar.selectbox("streamlit app", on_click=st.warning('This is a warning', icon="⚠️"), args=["home"])

#st.warning('This is a warning', icon="⚠️")

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()

#st.write("This is my new page!")

#def my_new_page():
#    st.write("This is my new page!")

st.sidebar.markdown("# Pages")
# st.sidebar.selectbox("streamlit app", on_click=st.session_state.set, args=["home"])
# st.sidebar.button("my new page", on_click=st.session_state.set, args=["my_new_page"])

# if st.session_state.get("page") == "my_new_page":
#    my_new_page()

#if os.path.isfile("streamlit_app.py"):
#    st.write("abcabcabc")

#st.write(os.path)
st.write(st.session_state.key)

#with st.sidebar:
#    st.[0]

"""
# Welcome to Streamlit! teste raul

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
