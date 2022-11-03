import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import csv
import filepaths
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode



# Initialization of the event variable
if "the_event" not in st.session_state:
    st.session_state['the_event'] = "0"

# my event
my_event = 0

#inlcude paths
csv_1 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_barc.csv"
csv_2 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/oly_pao.csv"
csv_3 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_bayern.csv"
fl_timetag = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\out.csv"
fl_vidfps = "E:\\Career files\Degree Thesis\\1. Coding general\\GIT project" \
               "\\Audiovisual-event-detection-and-localization-techniques-in-sport-content\\The final stack\\video_fps.txt"

# The title
st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)
# sidebar title
st.header(" Highlights of the Game 📸️")
st.sidebar.markdown("# Highlights of the Game 📸️️")

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


# make df clickable
def make_df(data):

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
    st.write(df)
    return df


# game options
my_options = ("Chose Game", "CSKA Moscow Vs Barcelona", "Olympiakos Vs Panathinaikos", "CSKA Moscow Vs Bayern Munich")
# make a menu
the_game = st.selectbox("What Game you want to watch Highlights from?", my_options, index=0, key=None,
                        help=None, on_change=None, args=None, kwargs=None,  disabled=False, label_visibility="visible")

# if statement for the games
if the_game == "CSKA Moscow Vs Barcelona":
    st.write('This is the ' + the_game + ' play by play text')
    df1 = pd.read_csv(csv_1)
    mydf = make_df(df1)
    vidflag = 1    # gia na steilo to video sto backend

elif the_game == "Olympiakos Vs Panathinaikos":
    st.write('This is the ' + the_game + ' play by play text')
    df2 = pd.read_csv(csv_2)
    mydf = make_df(df2)

elif the_game == "CSKA Moscow Vs Bayern Munich":
    st.write('This is the ' + the_game + ' play by play text')
    df3 = pd.read_csv(csv_3)
    mydf = make_df(df3)  # gia na steilo to video sto backend

elif the_game == "Chose Game":
    mydf = pd.DataFrame()

# If a game is chosen
if (not mydf.empty) and (the_game != "Chose Game"):
    my_event = mydf.iloc[0, 1]
    print("The timetag chosen by user is:", my_event)

    # store the event to pass it next page
    st.session_state.the_event = my_event
    #press button to watch it in the HomePage
    button_to_home = st.button("Watch the Highlight!")
    if button_to_home:
        switch_page('games videos')



