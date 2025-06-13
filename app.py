# Importing Libraries
import streamlit as st
import pandas as pd

# Full page
st.set_page_config(page_title="LPA", page_icon="Images/LPA Logo.png", layout="wide")

# Adding styles
with open("css/Style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Class Pages
class Pages:
    # Home page
    def home(self):        
        # img.image()

        with intro:
            st.title("Numeric Converter")
            st.write("🧠 **Smart Data Cleaner for Numeric Columns!**")
            st.write("Easily convert values that *look like numbers* but are actually stored as text or mixed types into real numeric values.")

            st.write("🔧 **Why use it?**")
            st.markdown("""
            - 🛠 Fix messy columns where numbers are stored as strings  
            - 📈 Prepare your data properly for analysis and modeling  
            - 💡 Avoid common errors like `'ValueError: could not convert string to float'`  
            """)

            start = st.button("Get Started", key="start")
            if start:
                st.session_state.select = "Howto"
                st.rerun()

    # HowTo page
    def howto(self):
        # img.image()

        with intro:
            st.write("📝 **How to Use:**")
            st.markdown("""
            1️⃣ *(Optional)* Create a copy of your DataFrame with only the columns you want to convert  
            2️⃣ Pass this DataFrame into the **Numeric Converter** App  
            3️⃣ It returns a clean DataFrame with values correctly typed as `int`, `float`, etc.
            """)
            st.write("✅ Perfect for preprocessing before EDA or machine learning!")

            # Result button
            start = st.button("Convert", key="convert")
            if start:
                st.session_state.select = "Result"
                st.rerun()

    # Result page
    def result(self):
        b1, txt, btn, b2 = st.columns([1, 10, 1, 1], vertical_alignment="center")

        txt.subheader("Numeric Converter has Succefully Converted your Dataset!")
        start = btn.button("Home", key="home")
        if start:
            st.session_state.select = "Home"
            st.rerun()

# Calling Pages
page_calls = Pages()

# Main Container
main_container = st.container(height=500, border=True)

with main_container:    
    b1,img,b2,intro,b3 = st.columns([0.2,2,0.2,2.5,0.4])

    if "select" not in st.session_state:
        st.session_state.select = "Home"

    if st.session_state.select == "Home":
        page_calls.home()
    elif st.session_state.select == "Howto":
        page_calls.howto()
    elif st.session_state.select == "Result":
        page_calls.result()