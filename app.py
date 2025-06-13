# Importing Libraries
import streamlit as st
import pandas as pd

# Full page
st.set_page_config(page_title="LPA", page_icon="Images/LPA Logo.png", layout="wide")

# Adding styles
with open("css/Style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
