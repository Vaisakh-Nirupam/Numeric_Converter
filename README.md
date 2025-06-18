# 🔢 Numeric Converter App

A smart and user-friendly **Streamlit** application that cleans up messy data by converting columns with text-based numbers into real numeric values — making your datasets analysis-ready in just a few clicks.

---

## 🌐 Live App

🔗 [Try the app now](https://numeric-converter.streamlit.app/)

---

## 🚀 Features

- 📤 Upload CSV files with mixed or messy data  
- 🔍 Automatically detect and convert object/text columns to numeric  
- 💡 Handles symbols (₹, €, $, %, etc.), alphabets, and punctuations  
- 📥 Download the cleaned dataset instantly  
- 🎨 Beautiful UI with custom images and CSS for enhanced UX  

---

## 🌟 Why Use This App?

If you’ve ever faced this:

```
ValueError: could not convert string to float: '₹5,000'
```

Then this tool is for you!

✅ Designed for data preprocessing before:

- Exploratory Data Analysis (EDA)  
- Machine Learning model training  
- Data visualization dashboards  

---

## 🛠️ Tech Stack

| Tool      | Description                    |
|-----------|--------------------------------|
| Streamlit | Interactive web app framework  |
| Pandas    | Data cleaning and manipulation |
| CSS       | Custom styling for UI          |

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/numeric-converter.git
cd numeric-converter
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the app**:

```bash
streamlit run app.py
```

> ✅ Make sure your file structure includes:
> - A `css/style.css` file for styling  
> - An `Images/` folder with `title.png`, `nums1.jpg`, and `nums2.jpg`

---

## 🖼️ Screenshots

- `Images/Demo1_Home.jpg` → Home Page  
- `Images/Demo2_Howto.jpg` → How To Use  
- `Images/Demo3_Result.jpg` → Result Page 

---

## 🧠 How It Works

1. Upload a CSV file containing textual or mixed numeric columns  
2. The app removes:
   - Punctuation symbols  
   - Currency signs and special characters  
   - Alphabets in mixed-type numeric columns  
3. Converts valid data to numeric format using `pandas.to_numeric()`  
4. Outputs a cleaned DataFrame ready for download or further processing  

---

## 👨‍💻 Author

**Vaisakh Nirupam**  
📫 [GitHub](https://github.com/Vaisakh-Nirupam)  
🔗 [LinkedIn](https://www.linkedin.com/in/vaisakh-nirupam)

---