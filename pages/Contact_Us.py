import streamlit as st
from send_email import send_email

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    options = ["Job Inquiries", "Project Proposals", "Other"]
    subject = st.selectbox("What topic do you want to discuss?", options)
    row_message = st.text_area("Your message")
    message = f"""\
Subject: {subject}

From: {user_email}
{row_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Send successfully!")