import streamlit as st
import filepaths
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page
from all_functions import match_scl, easyOcr_dir, tess_dir

####################################################### FILE PATHS ###############################################################
# init the styles of fonts
homepage = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>Homepage 🏠</strong></p>'
comp = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>Chose competition🏆</strong></p>'
title = '<p style="font-family:Arial Black; color:Chocolate; font-size: 300%; text-align: center;">SPORTS HIGHLIGHT GENERATOR 🏀</p>'

# Initialization of the event variable
if "timetags" not in st.session_state:
    st.session_state['timetags'] = "0"
# Initialization of the event variable
if "fps" not in st.session_state:
    st.session_state['fps'] = "0"

# Initialization of the event variable
if "the_event" not in st.session_state:
    st.session_state['the_event'] = "0"

######################################## THE LAYOUT OF THE PAGE ###########################################
#config of the page
st.set_page_config(page_title="SPORTS HIGHLIGHT GENERATOR🏀🏆", page_icon="🏀", layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)
# The title
#st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)

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
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

add_bg_from_url()

# set the homepage style
st.markdown(homepage, unsafe_allow_html=True)
st.write("\n")
st.write("\n")
st.write("\n")

################################################# CODE STUFF ######################################

# create 3 columns for each competition
st.markdown(comp,unsafe_allow_html=True)
st.write("\n")
st.write("\n")
col1, col2, col3 = st.columns(3, gap="large")

with col1:
   eurbut = st.button("Euroleague")
   #st.image("https://images.eurohoops.net/2019/05/ba5ac474-euroleague_logo-625x375.jpg")
   st.image("https://dd20lazkioz9n.cloudfront.net/wp-content/uploads/2021/06/Euroleague_Logo_Stacked.png")

with col2:
   nbabut = st.button("NBA")
   #st.image("https://andscape.com/wp-content/uploads/2017/06/nbalogo.jpg?w=700")
   st.image("https://1000logos.net/wp-content/uploads/2017/04/Logo-NBA.png")

with col3:
   grbut = st.button("Greek Basket League")
   #st.image("https://athlitikoskosmos.gr/wp-content/uploads/2022/10/inbound8215984157073710095.jpg")
   st.image("https://assets.b365api.com/images/wp/o/eff877d8fa1926f2f8423fa038e38f1a.png")


if eurbut:
    st.markdown("# Loading... Please wait🙂")
    # 2. get the matching frames with temp img with match_scl()
    myfps = match_scl(33.5, 34.5)
    st.session_state.fps = myfps
    # ocr the frames matching temp with easyOcr
    ttags, succ_r = easyOcr_dir()  # na ta kanw save kapou ta ttags
    # store ttags list for frontend
    st.session_state.timetags = ttags
    st.write("Redirecting to available Euroleague games...")
    switch_page("game highlights")

elif nbabut:
    st.sidebar.success("Not yet implemented")

elif grbut:
    st.sidebar.success("Not yet implemented")
