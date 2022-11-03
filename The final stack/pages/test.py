from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import csv
from all_functions import clip_creator
import filepaths


####################################################### FILE PATHS ###############################################################
fl_timetag = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\out.csv"
fl_vidfps = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\video_fps.txt"

# load timetags from file
my_tags = []
with open(fl_timetag, newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        my_tags.append(row)

# load fps from file
with open(fl_vidfps, "r") as file:
    my_fps = float(file.read())

st.write(st.session_state.the_event)
myevent = st.session_state.the_event


# create the Highlight clip if the timetag is correct
clip_creator(myevent, my_tags, my_fps, filepaths.f_path, filepaths.clip_1)
if 1:
    st.video(filepaths.clip_1, format="video/mp4", start_time=0)
else:
    print("The video doesnt exist")
