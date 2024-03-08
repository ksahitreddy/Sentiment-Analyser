# Save this code in a file, for example, app.py

import streamlit as st
import transformers
from transformers import pipeline

def process_input(user_input):
    sentiment = pipeline("sentiment-analysis", model='openai-community/gpt2')
    result = sentiment(user_input)
    return result[0]

st.set_page_config(layout="wide")

# Use local CSS to set the background image (using a URL)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://c4.wallpaperflare.com/wallpaper/215/545/101/sentimental-wallpaper-preview.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Creating a simple Streamlit web app interface
st.title('Sentiment Analyser')

# Text input from the user
user_input = st.text_input("Enter some text:")

if user_input:  # Check if the user has entered something
    # Process the input
    output = process_input(user_input)
    
    # Display the output
    st.write("Sentiment: "+output["label"])
