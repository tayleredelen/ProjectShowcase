import streamlit as st

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
    This page is a showcase of all the Python projects I created through the Python Mega Course. 
    """
    st.info(content)