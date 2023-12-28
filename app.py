# Q&A Chatbot
# from langchain.llms import OpenAI

from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo", layout="wide")

# Custom CSS to style the Streamlit app
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Layout
st.title("Gemini Application Demo", anchor=None)

# Columns for input and button
col1, col2 = st.columns(2)

with col1:
    input = st.text_area("Input your question here:", height=150, key="input")

with col2:
    submit = st.button("Ask the Question")

# If ask button is clicked, show response
if submit:
    with st.spinner('Waiting for response...'):
        response = get_gemini_response(input)
        st.subheader("Response")
        st.write(response)

# Add some space and a footer note
st.write("---")
st.markdown("*Built with Google Gemini by Pavan Belagatti for the Tutorial Purpose Only*")

