import streamlit as st
import pandas as pd

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


# ftiaxno ena koumpi gia na ginetai kati
button1 = st.button("CSKA Moscow Vs Barcelona", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
button2 = st.button("CSKA Moscow Vs Bayern Munich", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
button3 = st.button("Olympiakos Vs Panathinaikos", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)

if button1:
    st.write('This is the game video you chose')
    csv_1 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_barc.csv"
    df1 = pd.read_csv(csv_1)
    st.dataframe(df1)
elif button2:
    st.write('This is the game video you chose')
    csv_2 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/cska_bayern.csv"
    df2 = pd.read_csv(csv_2)
    st.dataframe(df2)
elif button3:
    st.write('This is the game video you chose')
    csv_3 = "E:\Career files\Degree Thesis/2. Dataset/play by play text/oly_pao.csv"
    df3 = pd.read_csv(csv_3)
    st.dataframe(df3)