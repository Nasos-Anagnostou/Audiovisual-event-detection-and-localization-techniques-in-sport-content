from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import csv
from all_functions import clip_creator
import filepaths
import streamlit
from PIL import Image



####################################################### FILE PATHS ###############################################################
img = Image.open("E://Career files//Degree Thesis/2. Dataset//template images//image2.jpg")

st.button(st.image(img))
