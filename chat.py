# Q&A Chatbot
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Google API
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

# Manage session state
if 'history' not in st.session_state:
    st.session_state['history'] = []

input = st.text_input("Input your question here:", key="input")
submit = st.button("Ask the Question")
clear = st.button("Clear Chat")

# If ask button is clicked
if submit:
    response = get_gemini_response(input)
    st.session_state['history'].append((input, response))
    for query, resp in st.session_state['history']:
        st.text_area("Question", value=query, height=100, disabled=True)
        for chunk in resp:
            st.text_area("Response", value=chunk.text, height=100, disabled=True)

# Clear chat history
if clear:
    st.session_state['history'] = []

# Footer
st.write("---")
st.markdown("*Built with Streamlit and Google Gemini*")
