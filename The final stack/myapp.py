import streamlit as st
import pandas as pd
from filepaths import file_paths

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

# The title
st.title("HIGHLIGHT GENERATOR 🏀🏆", anchor=None)
add_bg_from_url()

#2 tabs
tab1, tab2 = st.tabs(["Choose game", "Choose Highlight"])

with tab1:

    mylist = file_paths()



    # ftiaxno ena koumpi gia na ginetai kati
    button1 = st.button("Video", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
    button2 = st.button("Photo", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)
    button3 = st.button("Highlight Sheet", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)

    if button1:
        st.write('Why hello there')
        st.video(mylist[4], format="video/mp4", start_time=0)
    else:
        st.write('Goodbye')

    if button2:
        camera = st.camera_input("Camera", key=None, help=None, on_change=print("photo taken"), args=None, kwargs=None,
                                 disabled=False, label_visibility="visible")
    else:
        st.write('Goodbye')
    st.file_uploader("*Upload*", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None,
                     kwargs=None, disabled=False, label_visibility="visible")

    st.number_input("select game", min_value=0, max_value=10, value= 0, step=None, format=None, key=None, help=None,
                    on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    if button3:
        df = pd.read_csv(mylist[1])
        st.dataframe(df)


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

    name = st.text_input('Name')
    if not name:
        st.warning('Please input a name.')
        st.stop()
    st.success('Thank you for inputting a name.')