import streamlit as st
import filepaths
import os
import csv
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page
from all_functions import match_scl, easyOcr_dir, tess_dir

####################################################### INITIALIZATION ###############################################################
# init the styles of fonts
homepage = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>CREATOR OF HIGHLIGHTS 🏠</strong></p>'
comp = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>Chose competition🏆</strong></p>'
title = '<p style="font-family:Arial Black; color:Chocolate; font-size: 300%; text-align: center;">SPORTS HIGHLIGHT GENERATOR 🏀</p>'

# Initialization of the timetag variable
if "timetags" not in st.session_state:
    st.session_state['timetags'] = []

# Initialization of the fps variable
if "fps" not in st.session_state:
    st.session_state['fps'] = 25

# Initialization of the event variable
if "the_event" not in st.session_state:
    st.session_state['the_event'] = "0"

# Initialization of the game variable
if "the_game" not in st.session_state:
    st.session_state['the_game'] = 0

# Initialization of the event variable
if "competition" not in st.session_state:
    st.session_state['competition'] = "0"


######################################## THE LAYOUT OF THE PAGE ###########################################
#config of the page
st.set_page_config(page_title="SPORTS HIGHLIGHT GENERATOR🏀🏆", page_icon="🏀", layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)
# The title
#st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)

# insert empty spaces
def empty_line(lines_number):
    for num in range(lines_number):
        st.write("\n")

# set background wallpaper and subtitle title & sidebar name
def add_bg_from_url():
    st.markdown(
        f"""
       <style>
       .stApp {{
       background-image: url("https://abreuadvogados.com/wp-content/uploads/2021/02/Sports-Law-Portugal.jpg");
       background-attachment: fixed;
       background-size: cover
       }}
       </style>
       """,
        unsafe_allow_html=True
    )
    add_logo("https://i0.wp.com/www.esleschool.com/wp-content/uploads/2021/03/sports-1.png?resize=120%2C120&ssl=1")
    st.sidebar.markdown("# SPORTS HIGHLIGHT GENERATOR🏀🏆")
    # set the homepage style
    st.markdown(title, unsafe_allow_html=True)
    empty_line(4)

add_bg_from_url()

# set the homepage style
st.markdown(homepage, unsafe_allow_html=True)
empty_line(3)

################################################# CODE STUFF ######################################
# create 3 columns for each competition
st.markdown(comp,unsafe_allow_html=True)
empty_line(2)
col1, col2, col3 = st.columns(3, gap="large")
# game options to watch from
my_options = ("Choose from the available Games", "CSKA Moscow Vs Barcelona", "Olympiakos Vs Panathinaikos", "CSKA Moscow Vs Bayern Munich")

with col1:
    # st.image("https://images.eurohoops.net/2019/05/ba5ac474-euroleague_logo-625x375.jpg")
    st.image("https://dd20lazkioz9n.cloudfront.net/wp-content/uploads/2021/06/Euroleague_Logo_Stacked.png")
    # session competitions
    st.session_state.competition = "Euroleague"
    # user give how long the video will be
    start_min = st.text_input("Enter the starting minute", max_chars=5, placeholder="Starting minute")
    stop_min = st.text_input("Enter the stopping minute", max_chars=5, placeholder="Stopping minute")
    # make a menu with selectbox
    game_vid = st.selectbox("For which Game you want to create the Highlights?", my_options, index=0, key=None,
                            help=None, on_change=None, args=None, kwargs=None, disabled=False,
                            label_visibility="visible")
    # save game_vid value
    st.session_state.the_game = game_vid

    # if statement for the games
    if game_vid == "CSKA Moscow Vs Barcelona":
        st.write("Loading please wait... ⌚")
        # template matching and store fps
        myfps = match_scl(filepaths.trim_vid_eu1, filepaths.cska_barc_vid, filepaths.ocr_eu1, filepaths.tmp_eu,
                          float(start_min),float(stop_min))
        with open("video_fps.txt", "w") as file:
            file.write(str(myfps))

        # ocr the frames matching temp with easyOcr
        ttags, succ_r = easyOcr_dir(
            filepaths.ocr_eu1)  # na ta kanw save kapou ta ttags         # TA TTAGS GIA KATHE MATCH ALLO FAKELO
        with open(os.path.join(filepaths.timetags, "eur1.csv"), "w", newline='') as f:
            wr = csv.writer(f)
            wr.writerows(ttags)
        st.write("Thank you for your patience 🙂")

    elif game_vid == "Olympiakos Vs Panathinaikos":
        st.write("Loading please wait... ⌚")
        # template matching
        myfps = match_scl(filepaths.trim_vid_eu2, filepaths.oly_pao_csv_vid, filepaths.ocr_eu2, filepaths.tmp_eu, 33.5,
                          34.5)  # NA DINW THN TEMP IMAGE EDW
        with open("video_fps.txt", "w") as file:
            file.write(str(myfps))

        # ocr the frames matching temp with easyOcr
        ttags, succ_r = easyOcr_dir(
            filepaths.ocr_eu2)  # na ta kanw save kapou ta ttags         # TA TTAGS GIA KATHE MATCH ALLO FAKELO
        with open(os.path.join(filepaths.timetags, "eur2.csv"), "w", newline='') as f:
            wr = csv.writer(f)
            wr.writerows(ttags)
        st.write("Thank you for your patience 🙂")

    elif game_vid == "CSKA Moscow Vs Bayern Munich":
        st.write("Loading please wait... ⌚")
        # template matching
        myfps = match_scl(filepaths.trim_vid_eu3, filepaths.cska_bayern_vid, filepaths.ocr_eu3, filepaths.tmp_eu, 33.5,
                          34.5)  # NA DINW THN TEMP IMAGE EDW
        with open("video_fps.txt", "w") as file:
            file.write(str(myfps))

        # ocr the frames matching temp with easyOcr
        ttags, succ_r = easyOcr_dir(
            filepaths.ocr_eu3)  # na ta kanw save kapou ta ttags         # TA TTAGS GIA KATHE MATCH ALLO FAKELO
        with open(os.path.join(filepaths.timetags, "eur3.csv"), "w", newline='') as f:
            wr = csv.writer(f)
            wr.writerows(ttags)
        st.write("Thank you for your patience 🙂")


with col2:
   # st.image("https://andscape.com/wp-content/uploads/2017/06/nbalogo.jpg?w=700")
   st.image("https://1000logos.net/wp-content/uploads/2017/04/Logo-NBA.png")


with col3:
   #st.image("https://athlitikoskosmos.gr/wp-content/uploads/2022/10/inbound8215984157073710095.jpg")
   st.image("https://assets.b365api.com/images/wp/o/eff877d8fa1926f2f8423fa038e38f1a.png")




