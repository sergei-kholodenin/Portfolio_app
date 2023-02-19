import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company")

content = """"
We are a company that develops and implements web applications, tools and websites. Our wide range of services covers any industry, and leading experts will help you choose the best option for your company.
 You will be able to implement your ideas in the shortest possible time, and we will help you with this. Contact us now.
"""

st.write(content)

st.header("Our team")

col1, empty1, col2, empty2, col3, empty3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5, 0.5])

df = pd.read_csv("data.csv", sep=";")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row['image'])

