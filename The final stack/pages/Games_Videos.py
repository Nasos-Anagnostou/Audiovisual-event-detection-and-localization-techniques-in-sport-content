from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import csv
from all_functions import clip_creator
import filepaths
from HomePage import add_bg_from_url


####################################################### FILE PATHS ###############################################################
fl_timetag = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\out.csv"
fl_vidfps = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\video_fps.txt"


######################################## THE LAYOUT OF THE PAGE ###########################################
# add the background image
add_bg_from_url()
# The title
st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)
st.markdown("# Game Videos 📺")
st.write("\n")
# sidebar title
st.sidebar.markdown("# Game Videos 📺")
# return to homepage button
if st.sidebar.button("Return to Homepage🏠"):
    switch_page('homepage')
elif st.sidebar.button("Chose again Highlight 📸"):
    switch_page("game highlights")


# load timetags from file
my_tags = []
with open(fl_timetag, newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        my_tags.append(row)

# load fps from file
with open(fl_vidfps, "r") as file:
    my_fps = float(file.read())

# get the stored event from another page
myevent = st.session_state.the_event

# create the Highlight clip if the timetag is correct else display error message
vid_exist = clip_creator(myevent, my_tags, my_fps, filepaths.f_path, filepaths.clip_1)
if vid_exist:
    st.video(filepaths.clip_1, format="video/mp4", start_time=0)
else:
    st.write("We are sorry 😏, the Highlight you want to watch doesnt exist in our database")
