from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables and configure the API
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error("Error in getting response: " + str(e))
        return None

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

# Custom CSS for styling
st.markdown("""
<style>
body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    background-color: #f4f4f2;
    color: #333;
}
h1 {
    color: #0b5d8c;
}
.stButton>button {
    color: white;
    background-color: #0b5d8c;
    border-radius: 5px;
    padding: 10px 24px;
}
</style>
""", unsafe_allow_html=True)

st.header("Gemini LLM Application")

# Manage input and session state
input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input:
    with st.spinner('Fetching response...'):
        response = get_gemini_response(input)
    if response:
        st.session_state['chat_history'].append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state.get('chat_history', []):
    st.text(f"{role}: {text}")

# Footer and additional info
st.markdown('---')
st.markdown('<p class="small-font">Built with ❤️ and Streamlit</p>', unsafe_allow_html=True)
    



    

