import streamlit as st
from filepaths import file_paths

tab1, tab2 = st.tabs(["Choose game", "Choose Highlight"])

with tab1:
    st.radio('Select one:', [1, 2])

    mylist = file_paths()

    def add_bg_from_url():
        st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("https://wallpaper.dog/large/968252.jpg");
        background-attachment: fixed;
        background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_url()

    st.button("select", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)
    st.number_input("select game", min_value=0, max_value=1000, value= 0, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")


with tab2:

    #st.image("https://wallpaper.dog/large/968252.jpg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    with st.form("my_form"):
       st.write("Inside the form")
       slider_val = st.slider("Form slider")
       checkbox_val = st.checkbox("Form checkbox")

       # Every form must have a submit button.
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")


    st.video(mylist[4], format="video/mp4", start_time=0)