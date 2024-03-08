import streamlit as st
import transformers
from transformers import pipeline

def process_input(user_input):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(user_input)
    return result[0]

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://t3.ftcdn.net/jpg/07/27/45/88/360_F_727458823_OUK5bNdtNwRhHs4pdLcHdjav2CZbJ7Z8.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('Sentiment Analyser')

user_input = st.text_input("Enter some text:")

if user_input: 
    
    output = process_input(user_input)
    
    st.write("Sentiment: "+output["label"])
