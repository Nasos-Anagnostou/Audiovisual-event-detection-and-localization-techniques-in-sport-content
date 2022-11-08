from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import csv
from all_functions import clip_creator
from HomePage import add_bg_from_url
import filepaths


####################################################### FILE PATHS ###############################################################
fl_timetag = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\out.csv"
fl_vidfps = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\video_fps.txt"


######################################## THE LAYOUT OF THE PAGE ###########################################
#config of the page
st.set_page_config(page_title="SPORTS HIGHLIGHT GENERATOR🏀🏆", page_icon="🏀", layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)

gamevideos = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>Game Videos 📺</strong></p>'

# add the background image
add_bg_from_url()
st.markdown(gamevideos, unsafe_allow_html=True)
st.write("\n")
# # sidebar title
# st.sidebar.markdown("# Game Videos 📺")
# return to homepage button
if st.sidebar.button("🏠Return to Homepage"):
    switch_page('homepage')
elif st.sidebar.button("📸Watch another Highlight"):
    switch_page("game highlights")


################################################# CODE STUFF #################################################
# load timetags from file
my_tags = []
with open(fl_timetag, newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        my_tags.append(row)

# # load fps from file
# with open(fl_vidfps, "r") as file:
#     my_fps = float(file.read())

my_fps = st.session_state.fps

# get the stored event from another page
my_event = st.session_state.the_event

# create the Highlight clip if the timetag is correct else display error message
vid_exist, videoclip = clip_creator(my_event, my_tags, my_fps)
if vid_exist:
    st.video(videoclip, format="video/mp4", start_time=0)
else:
    st.write("We are sorry 😏, the Highlight you want to watch doesnt exist in our database")
