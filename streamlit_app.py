from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.session_state.key = 'home'

def my_new_page():
    st.write("This is my new page!")

st.sidebar.markdown("# Pages")
# st.sidebar.button("Home", on_click=st.session_state.set, args=["home"])
# st.sidebar.button("My new page", on_click=st.session_state.set, args=["my_new_page"])

if st.session_state.get("page") == "my_new_page":
    my_new_page()


with st.sidebar:

	st.markdown('### Filtros de paradas')
	with st.form(key="completez"):
		inicio_fecha = st.date_input(label="Fecha de inicio")
		final_fecha = st.date_input(label="Fecha final")
		id_camion = st.selectbox(label="Seleccione un vehiculo:", options=[13, 14, 15])
		hexagono_size = 10#st.slider(label="Tamaño de hexagonos", min_value=0, max_value=15, step=1, value=11)

		estadistica = st.form_submit_button("Enviar")

st.markdown(st.session_state.get("page"))


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
