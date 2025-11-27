import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Latest Flash model
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot using GenAI")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Study Buddy prompt
    prompt = f"""
You are a Study Buddy AI for beginners.
Explain answers in very simple language.
Give short examples.
If user asks unrelated questions, guide them back politely.

User: {user_input}
"""
    response = model.generate_content(prompt).text

    # Show bot response
    st.session_state.messages.append({"role": "assistant", "text": response})
    with st.chat_message("assistant"):
        st.markdown(response)
