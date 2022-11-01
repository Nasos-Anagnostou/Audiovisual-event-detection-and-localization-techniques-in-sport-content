import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# The title
st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)

st.markdown("# Game Videos 📺")
st.sidebar.markdown("# Game Videos 📺")
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


def make_df(data):
    #data = pd.read_csv("E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_barc.csv")
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
    gb.configure_side_bar()  # Add a sidebar
    gb.configure_selection('single', use_checkbox=True,
                           groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
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
    mydf = st.write(df)
    return mydf


# ftiaxno 3 button 1h proseggisi
#button1 = st.button("CSKA Moscow Vs Barcelona", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
#button2 = st.button("CSKA Moscow Vs Bayern Munich", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
#button3 = st.button("Olympiakos Vs Panathinaikos", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)

# if button1:
#     st.write('This is the CSKA Moscow Vs Barcelona play by play text')
#     csv_1 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_barc.csv"
#     df1 = pd.read_csv(csv_1)
#     make_df(df1)
#     #st.dataframe(df1)
# elif button2:
#     st.write('This is the CSKA Moscow Vs Bayern Munich play by play text')
#     csv_2 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_bayern.csv"
#     df2 = pd.read_csv(csv_2)
#     make_df(df2)
#     #st.dataframe(df2)
# elif button3:
#     st.write('This is the Olympiakos Vs Panathinaikos play by play text')
#     csv_3 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/oly_pao.csv"
#     df3 = pd.read_csv(csv_3)
#     make_df(df3)
#     #st.dataframe(df3)



#Create 3 tabs 2h proseggisi
tab1, tab2, tab3 = st.tabs(["CSKA Moscow Vs Barcelona ", "Olympiakos Vs Panathinaikos", "CSKA Moscow Vs Bayern Munich"])


with tab1:
    st.write('This is the CSKA Moscow Vs Barcelona play by play text')
    csv_1 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_barc.csv"
    df1 = pd.read_csv(csv_1)
    make_df(df1)

with tab2:
    st.write('This is the CSKA Moscow Vs Bayern Munich play by play text')
    csv_2 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_bayern.csv"
    df2 = pd.read_csv(csv_2)
    make_df(df2)

with tab3:
    st.write('This is the Olympiakos Vs Panathinaikos play by play text')
    csv_3 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/oly_pao.csv"
    df3 = pd.read_csv(csv_3)
    make_df(df3)

