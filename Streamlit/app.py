import streamlit as st
import pandas as pd
import numpy as np

## Title of the app
st.title("Hello Streamlit App")

## Display a simple text
st.write("Welcome to Streamlit! This is a simple app to demonstrate its capabilities.")

## Create a simple DataFrame
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

## Display the DataFrame
st.write("Here is a simple DataFrame:")
st.dataframe(df)

## Create a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)