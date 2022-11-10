import streamlit as st


col1, col2, col3 = st.columns(3)
if col1.button('Click'):
    st.write('hello')