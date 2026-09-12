import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
st.set_page_config(page_title="AI Career Advisor", page_icon="🤖")

# Load the secret key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Connect to Groq (it works like OpenAI but points to Groq's servers)
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

st.title("🤖 My AI Career Advisor")

if st.button("🗑️ Clear Conversation"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly, encouraging career advisor for engineering students looking for their first job."}
    ]
    st.rerun()

# Keep chat history so the bot remembers the conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly, encouraging career advisor for engineering students looking for their first job."}
    ]
# Quick-start prompt buttons
st.write("Try asking:")
col1, col2, col3 = st.columns(3)
quick_prompt = None

with col1:
    if st.button("💼 Interview tips"):
        quick_prompt = "What are the best tips to prepare for a technical interview as a fresher?"
with col2:
    if st.button("📄 Resume advice"):
        quick_prompt = "What should I include in my resume as a fresher engineering student?"
with col3:
    if st.button("📈 Trending skills"):
        quick_prompt = "What skills are currently in demand for fresher software engineering roles?"
# Show previous messages on screen
for msg in st.session_state.messages[1:]:  # skip the system message
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Take new input from user
# Take new input from user
user_input = st.chat_input("Ask me anything about your career...")

# If a quick-start button was clicked, use that instead
if quick_prompt:
    user_input = quick_prompt

if user_input:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI's reply
       # Get AI's reply
     # Get AI's reply
    try:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content

        # Show AI's reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)

    except Exception as e:
        with st.chat_message("assistant"):
            st.write("Sorry, I'm having trouble responding right now. Please try again in a moment! 🙏")