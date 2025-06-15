# Importing Libraries
import streamlit as st
import pandas as pd

# Full page
st.set_page_config(page_title="Numeric Converter", page_icon="Images/.png", layout="wide")

# Adding styles
with open("css/Style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Numeric Converter Function
def Numeric_Converter(df):
  df_cpy = df.copy()
  df_cpy.dropna(inplace=True)
  dfc = df_cpy.copy()

  for i in dfc:
    if dfc[i].dtype == 'object':

          pun = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~₹€£'
          alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
          dfc[i] = dfc[i].apply(func = lambda x : x.split()[0])

          for j in pun:
            dfc[i] = dfc[i].str.replace(j,"")

          if dfc[i].str.isalpha().all():
            continue

          for k in alp:
            dfc[i] = dfc[i].str.replace(k,"")
          else:
            df_cpy[i] = pd.to_numeric(dfc[i], errors="coerce")

  return df_cpy

# Page Title
st.image("")

# Class Pages
class Pages:
    # Home page
    def home(self):        
        img.image("Images/nums1.jpg")

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
        img.image("Images/nums2.jpg")
        
        with intro:
            st.title("📝 **How to Use:**")
            st.markdown("""
            1️⃣ *(Optional)* Create a copy of your DataFrame with only the columns you want to convert  
            2️⃣ Upload the CSV file using the uploader below  
            3️⃣ Click Convert to run the **Numeric Converter**  
            """)

            st.write("✅ Perfect for preprocessing before EDA or machine learning!")

            # File uploader
            uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])
            
            # Buttons layout
            conv, stat, b = st.columns([1.5, 4, 1], vertical_alignment="top")
            
            if uploaded_file is not None:
                try:
                    df = pd.read_csv(uploaded_file)
                    st.session_state.original_df = df
                    stat.success("✅ File uploaded successfully!")
                except Exception as e:
                    st.error(f"❌ Error reading file: {e}")

            # Result button
            start = conv.button("Convert", key="convert")
            if start:
                if "original_df" in st.session_state:
                    result = Numeric_Converter(st.session_state.original_df)
                    st.session_state.converted_df = result
                    st.session_state.select = "Result"
                    st.rerun()
                else:
                    stat.warning("⚠️ Please upload a CSV file first!")

    # Result page
    def result(self):
        b1, txt, btn1, btn2, b2 = st.columns([1, 3, 1, 1, 1], vertical_alignment="top")

        txt.subheader("🎯 Your Cleaned Dataset is Ready:")

        if "converted_df" in st.session_state:
            df = st.session_state.converted_df
            st.dataframe(df, use_container_width=True, height=350)

            # CSV download button
            csv = df.to_csv(index=False).encode('utf-8')
            btn1.download_button(label="Download CSV", data=csv, file_name="converted_dataset.csv", mime="text/csv")
        else:
            st.warning("⚠️ No data found. Please go back and upload a CSV file first.")

        start = btn2.button("Home", key="home")
        if start:
            st.session_state.select = "Home"
            st.rerun()

# Calling Pages
page_calls = Pages()

# Main Container
main_container = st.container(height=500, border=True)

with main_container:    
    b1,img,b2,intro,b3 = st.columns([0.2,2,0.2,2.2,0.4])

    # Page navigation
    if "select" not in st.session_state:
        st.session_state.select = "Home"

    if st.session_state.select == "Home":
        page_calls.home()
    elif st.session_state.select == "Howto":
        page_calls.howto()
    elif st.session_state.select == "Result":
        page_calls.result()