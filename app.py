import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the secret key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Connect to Groq (it works like OpenAI but points to Groq's servers)
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

st.title("🤖 My AI Career Advisor")

# Keep chat history so the bot remembers the conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly, encouraging career advisor for engineering students looking for their first job."}
    ]

# Show previous messages on screen
for msg in st.session_state.messages[1:]:  # skip the system message
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Take new input from user
user_input = st.chat_input("Ask me anything about your career...")

if user_input:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI's reply
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content

    # Show AI's reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)