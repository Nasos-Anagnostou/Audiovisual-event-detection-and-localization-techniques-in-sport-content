import streamlit as st


# The title
st.title("SPORTS HIGHLIGHT GENERATOR 🏀", anchor=None)

st.markdown("# Highlights of the Game 📸️")
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