import streamlit as st

def my_new_page():
    st.write("This is my new page!")

st.session_state.key = 'my_new_page'

st.write(st.session_state.key)

st.write(st.session_state.get("page"))

# st.sidebar.markdown("# Pages")
st.sidebar.selectbox("streamlit app", on_click=st.session_state.key, args=['home'])
st.sidebar.button("my new page", on_click=st.session_state.key, args=['my_new_page'])
# st.sidebar.button("My new page", on_click=st.session_state.set, args=["my_new_page"])

#if st.session_state.get("page") == "my_new_page":
#    my_new_page()

st.markdown(st.session_state.get("page"))
