import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name", "Type here...")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

options = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Select your favorite programming language", options)
st.write(f"You selected: {choice}")

if name :
    st.write(f"Hello, {name}!")
    
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
st.write("Here is a sample DataFrame:")
st.dataframe(df)

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    df_uploaded = pd.read_csv(upload_file)
    st.write("Uploaded DataFrame:")
    st.dataframe(df_uploaded)

 
    
    