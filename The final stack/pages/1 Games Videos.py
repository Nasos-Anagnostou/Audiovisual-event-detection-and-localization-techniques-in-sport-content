import streamlit as st

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
button1 = st.button("Game number 1", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
button2 = st.button("Game number 2", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
button3 = st.button("Game number 3", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)

if button1:
    st.write('This is the game video you chose')
    csv_1 = /2. Dataset/play by play text/cska_barc.csv"
    df = pd.read_csv(mylist[2])
    st.dataframe(df)
elif button2:
    st.write('This is the highlight you wanted')
    df = pd.read_csv(mylist[2])
    st.dataframe(df)
elif button3:
    st.write('This is the highlight you wanted')
    df = pd.read_csv(mylist[2])
    st.dataframe(df)