import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Tayler Edelen")
    content = """
    Hiya, I'm Tayler! I am a seasoned finance pro turned programmer. 
    In August 2023 I graduated from the coding bootcamp LaunchCode in STL. 
    I learned Java and JavaScript, and applied them through full-stack web development. 
    Learning Python I am continuing to satisfy my technological curiosities.  
    """
    st.info(content)

content2 = """
Below are Python projects I created through the Udemy Python Mega Course.
Feel free to contact me! 
"""
st.write(content2)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
# tells pandas to read csv and separate data by semicolon

with col3:
    for index, row in df.iterrows():
        st.header(row["title"])


with col4:
    for index, row in df.iterrows():
        st.header(row["title"])

