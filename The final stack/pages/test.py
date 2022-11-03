from streamlit_extras.switch_page_button import switch_page
import streamlit as st

want_to_contribute = st.button("Return to Homepage!")
if want_to_contribute:
    switch_page('homepage')
