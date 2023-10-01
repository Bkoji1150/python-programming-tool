import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv("topics.csv")
topics = df['topic']

st.header("Contact Me")
with st.form(key="email_form"):

    user_email = st.text_input("Your email address")
    topic_discussion = st.selectbox('What topic do you want to discuss?', topics)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic_discussion}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully.!")
