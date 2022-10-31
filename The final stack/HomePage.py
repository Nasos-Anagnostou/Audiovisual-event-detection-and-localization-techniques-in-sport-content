import streamlit as st
import pandas as pd
from filepaths import file_paths

st.set_page_config(page_title="SPORTS HIGHLIGHT GENERATOR🏀🏆", page_icon="🏀", layout="centered",
                   initial_sidebar_state="auto", menu_items=None)

# background wallpaper set
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

st.markdown("# SPORTS HIGHLIGHT GENERATOR 🏀")
st.sidebar.markdown("# SPORTS HIGHLIGHT GENERATOR 🏀🏆")

#parse the filepaths
mylist = file_paths()

# The title
#st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)

#Create 2 tabs
tab1, tab2 = st.tabs(["Choose game", "Choose Highlight"])

#Tab n1
with tab1:

# ftiaxno ena koumpi gia na ginetai kati
    button1 = st.button("Game Video", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
    button2 = st.button("Photo", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)
    button3 = st.button("Highlight Sheet", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)

# enallagi features metaksu koumpion
    if button1:
        st.write('This is the highlight you wanted')
        st.video(mylist[7], format="video/mp4", start_time=0)
    elif button2:
        camera = st.camera_input("Camera", key=None, help=None, on_change=None, args=None, kwargs=None,
                                 disabled=False, label_visibility="visible")


    st.file_uploader("*Upload*", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None,
                     kwargs=None, disabled=False, label_visibility="visible")

    st.number_input("select game", min_value=0, max_value=10, value= 0, step=None, format=None, key=None, help=None,
                    on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    if button3:
        df = pd.read_csv(mylist[2])
        st.dataframe(df)

#Tab n2
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


    st.video(mylist[7], format="video/mp4", start_time=0)

    name = st.text_input('Name')
    if not name:
        st.warning('Please input a name.')
        st.stop()
    st.success('Thank you for inputting a name.')