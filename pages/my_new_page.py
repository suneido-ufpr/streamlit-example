import streamlit as st

st.title('my_new_page x')

if 'my_new_page' not in st.session_state:
    st.session_state.my_new_page = 'my_new_page'

if 'home' not in st.session_state:
    st.session_state.home = 'home'

# Adiciona um link para a página "My new page" ao menu lateral
st.sidebar.write(f"**[My new page](?page=my_new_page)**")

# Cria o menu
st.sidebar.markdown("# Pages")
st.sidebar.button("streamlit app", on_click=st.session_state.home)
st.sidebar.button("my new page")

'''
import streamlit as st

st.title('my_new_page x')

if 'my_new_page' not in st.session_state:
    st.session_state.my_new_page = 'my_new_page'

if 'home' not in st.session_state:
    st.session_state.home = 'home'



st.sidebar.button("streamlit app", on_click=st.session_state.home, args=['home'])
st.sidebar.button("my new page", on_click=st.session_state.my_new_page, args=['my_new_page'])
'''



'''

def my_new_page_write():
    st.write("This is my new page!")

#st.write('Count = ', st.session_state.count)



def my_new_page():
    st.write("This is my new page!")

st.session_state.key = 'my_new_page'
st.write(st.session_state.key)
st.write(st.session_state.get("page"))

# st.sidebar.markdown("# Pages")
st.sidebar.button("streamlit app", on_click=st.session_state.set, args=["home"])
st.sidebar.button("my new page", on_click=st.session_state.set, args=['my_new_page'])
# st.sidebar.button("My new page", on_click=st.session_state.set, args=["my_new_page"])

#if st.session_state.get("page") == "my_new_page":
#    my_new_page()

st.markdown(st.session_state.get("page"))
'''