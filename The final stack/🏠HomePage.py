import streamlit as st
import pandas as pd

from filepaths import file_paths

Game_Highlights = __import__('pages.02_📸_Game_Highlights.py')


#config of the page
st.set_page_config(page_title="SPORTS HIGHLIGHT GENERATOR🏀🏆", page_icon="🏀", layout="wide",
                   initial_sidebar_state="auto", menu_items=None)

# The title
st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)


# set background wallpaper and subtitle title & sidebar name
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
    st.markdown("# Homepage 🏀")
    st.sidebar.success("Select one of the above pages")
add_bg_from_url()

################################################# CODE STUFF ######################################
st.write(2)
#parse the filepaths
mylist = file_paths()


# #Create 2 tabs
# tab1, tab2 = st.tabs(["Choose game", "Choose Highlight"])
#
# #Tab n1
# with tab1:
#
# # ftiaxno ena koumpi gia na ginetai kati
#     button1 = st.button("Game Video", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
#     button2 = st.button("Photo", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)
#     button3 = st.button("Highlight Sheet", key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)
#
# # enallagi features metaksu koumpion
#     if button1:
#         st.write('This is the highlight you wanted')
#         st.video(mylist[7], format="video/mp4", start_time=0)
#     elif button2:
#         camera = st.camera_input("Camera", key=None, help=None, on_change=None, args=None, kwargs=None,
#                                  disabled=False, label_visibility="visible")
#     elif button3:
#         df = pd.read_csv(mylist[2])
#         st.dataframe(df)
#
#
# #testing upload
#     st.file_uploader("*Upload*", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None,
#                      kwargs=None, disabled=False, label_visibility="visible")
#
# #testing number input
#     st.number_input("select game", min_value=0, max_value=10, value= 0, step=None, format=None, key=None, help=None,
#                     on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
#
#
# #Tab n2
# with tab2:
#
#     #st.image("https://wallpaper.dog/large/968252.jpg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
#     with st.form("my_form"):
#        st.write("Inside the form")
#        slider_val = st.slider("Form slider")
#        checkbox_val = st.checkbox("Form checkbox")
#
#        # Every form must have a submit button.
#        submitted = st.form_submit_button("Submit")
#        if submitted:
#            st.write("slider", slider_val, "checkbox", checkbox_val)
#
#     st.write("Outside the form")
#
#
#     st.video(mylist[7], format="video/mp4", start_time=0)
#
#     name = st.text_input('Name')
#     if not name:
#         st.warning('Please input a name.')
#         st.stop()
#     st.success('Thank you for inputting a name.')


"st.session_state.object:", st.session_state

number = st.slider("A number", 1, 10, key = "slider")


st.write(st.session_state)

