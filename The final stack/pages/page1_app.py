import streamlit as st

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
button1 = st.button("Game number1", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
button2 = st.button("Game number2", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)
button3 = st.button("Game number3", key=None, help=None, on_click = None, args=None, kwargs=None, disabled=False)