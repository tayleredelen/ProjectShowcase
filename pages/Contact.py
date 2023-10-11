import streamlit as st
from send_email import send_email

st.header("Contact Me")
st.write("Please complete the below form to contact Tayler")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    # text_area allows multi-line entry
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Message: {raw_message}
"""
    button = st.form_submit_button("Submit")
    # special button for form submission
    if button:
        send_email(message)
        st.info("Your email was sent successfully")