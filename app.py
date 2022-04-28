import openai
import os
import streamlit as st
from main import wish

# Setting the API key for the OpenAI API.
openai.api_key = os.getenv("OPENAI_API_KEY")

st.header("🌸 Wish your special ones on an occasion!")
st.write("An app by Shyamal Anadkat")

form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    # Creating a text input box for the user to enter the name of the person they want to wish.
    subject = cols[0].text_input("Who are you wishing?")
    occasion = cols[1].selectbox(
        "What is the occasion?",
        (
            "Birthday",
            "Anniversary",
            "Graduation",
            "Engagement",
            "Retirement",
            "Journey",
        ),
    )
    submitted = st.form_submit_button(label="Submit")

if submitted:
    # Calling the `wish` function from the `main.py` file.
    st.write(wish(subject, occasion))
    st.balloons()
