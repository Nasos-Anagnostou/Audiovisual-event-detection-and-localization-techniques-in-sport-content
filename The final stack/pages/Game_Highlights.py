import os.path
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from HomePage import add_bg_from_url, empty_line
import filepaths
from all_functions import clip_creator
import csv
from PIL import Image




# euroleague games
euro_games = ("Choose from the available Games", "CSKA Moscow Vs Barcelona", "Olympiakos Vs Panathinaikos", "CSKA Moscow Vs Bayern Munich")
eur1_ttag = filepaths.timetags + "/eur1.csv"
#nba games
nba_games = ("none")
# basket league games
grbl_games = ("none")

######################################## THE LAYOUT OF THE PAGE ###########################################
gamevideo = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>Watch the Video 📺</strong></p>'
highlights = '<p style="font-family:Arial Black; color:#262730; font-size: 200%;"><strong>Highlights of the Game 📸️</strong></p>'
err_message = '<p style="font-family:Arial Black; color:coral; font-size: 100%;"><strong>Choose a competition from the HomePage first please 🙂</strong></p>'

#config of the page
st.set_page_config(page_title="SPORTS HIGHLIGHT GENERATOR🏀🏆", page_icon="🏀", layout="wide",
                   initial_sidebar_state="expanded", menu_items=None)

# add the background image
add_bg_from_url()

# # sidebar title
# st.sidebar.markdown("# Highlights of the Game 📸️")
# return to homepage button
if st.sidebar.button("🏠Return to Homepage"):
    switch_page('homepage')

################################################# CODE STUFF #################################################
col1, col2 = st.columns(2, gap="large")
# make Dataframes clickable
def make_df(data,vid_dir, ttag_dir):

    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
    gb.configure_side_bar()  # Add a sidebar
    gb.configure_selection('single', use_checkbox=False, groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=True,
        theme='balham',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=750,
        width="Any",
        reload_data=False
    )
    data = grid_response['data']
    selected = grid_response['selected_rows']
    df = pd.DataFrame(selected)  # Pass the selected rows to a new dataframe df
    df = df.iloc[:, 1:]

    # session flag
    st.session_state.flag = False
    # # If a game is chosen  store the event to pass it next page !! CLICK !!
    if (not df.empty) and (game_vid != "Chose from the available Games"):
        # get the stored event from another page
        with open(os.path.join(filepaths.timetags, ttag_dir), newline='') as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                st.session_state.timetags.append(row)

        st.session_state.the_vid = vid_dir
        st.session_state.the_event = df.iloc[0, 1]
        #switch_page('games videos')                # EPILOGI 1 TON PIGAINO STO VIDEOS
        st.session_state.flag = True

    return df

with col1:
    # title of the page
    st.markdown(highlights, unsafe_allow_html=True)

    # session competition
    my_comp = st.session_state.competition
    # if statement for the games
    if my_comp == "Euroleague":

        # make a menu with selectbox
        game_vid = st.selectbox("What Game you want to watch Highlights from?", euro_games, index=0, key=None,
                                help=None, on_change=None, args=None, kwargs=None, disabled=False,
                                label_visibility="visible")
        # session game
        st.session_state.the_game = game_vid
        # if statement for the games
        if game_vid == "CSKA Moscow Vs Barcelona":
            st.write('This is the ' + game_vid + ' play by play text')
            df1 = pd.read_csv(filepaths.cska_barc_csv)
            make_df(df1, filepaths.trim_vid_eu1, "eur1.csv")

        elif game_vid == "Olympiakos Vs Panathinaikos":
            st.write('This is the ' + game_vid + ' play by play text')
            df2 = pd.read_csv(filepaths.oly_pao_csv)
            make_df(df2, filepaths.trim_vid_eu2, "eur2.csv")

        elif game_vid == "CSKA Moscow Vs Bayern Munich":
            st.write('This is the ' + game_vid + ' play by play text')
            df3 = pd.read_csv(filepaths.cska_bayern_csv)
            make_df(df3, filepaths.trim_vid_eu3, "eur3.csv")  # gia na steilo to video sto backend

        else:
            st.session_state.flag = False

    elif my_comp == "Nba":
        st.write("Load the games of Nba first")
        st.image("https://qrs.in/frontent/images/noresult.png")

    elif my_comp == "Basket League":
        st.write("Load the games of Basket League first")
        st.image("https://qrs.in/frontent/images/noresult.png")
    else:
        empty_line(3)
        st.markdown(err_message, unsafe_allow_html=True)
        empty_line(2)
        st.image("https://qrs.in/frontent/images/noresult.png")


with col2:                                              # EPILOGI 2 TA EMFANIZO DIPLA
    # title of the page
    st.markdown(gamevideo, unsafe_allow_html=True)
    empty_line(5)
    # load the inputs for the video
    my_event = st.session_state.the_event
    my_tags = st.session_state.timetags
    my_vid = st.session_state.the_vid
    #empty_line(8)
    # create the Highlight clip if the timetag is correct else display error message
    vid_exist, videoclip = clip_creator(my_vid, my_event, my_tags, 25)
    if vid_exist:
        # create a nice temple for video
        image1 = Image.open('C://Users//Nasos//Desktop//upper.jpg')
        st.image(image1)

        st.video(videoclip, format="video/mp4", start_time=0)

        image2 = Image.open('C://Users//Nasos//Desktop//lower.jpg')
        st.image(image2)

    elif not vid_exist and not st.session_state.fps:
        st.write("Please select a Highlight on the sheet left 📃")


    elif not vid_exist and st.session_state.fps:
        st.write("We are sorry 😏, the Highlight you want to watch doesnt exist in our database")
    # if not vid_exist and my_event == '0':
    #     st.write("Please select the highlight you want to watch")
    #
    # elif not vid_exist and my_event != '0':
    #     st.write("We are sorry 😏, the Highlight you want to watch doesnt exist in our database")
    #
