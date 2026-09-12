# 🤖 AI Career Advisor Chatbot

A conversational AI assistant built to give quick, practical career guidance for engineering students — interview tips, resume advice, and insights on in-demand skills.

## 🔗 Live Demo
[Try it here](https://ai-career-chatbot-5ezrzb7ka5mr6fvwyddpz4.streamlit.app/)

## 🛠️ Built With
- **Python**
- **Streamlit** – for the chat interface
- **Groq API** – LLM inference (openai/gpt-oss-120b)
- **python-dotenv** – secure API key management

## ✨ Features
- Persistent chat history within a session
- Quick-start prompt buttons (Interview tips, Resume advice, Trending skills)
- Clear conversation button
- Graceful error handling
- Secrets managed securely (never hardcoded)

## 🚀 Running Locally
1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with your key: `GROQ_API_KEY=your_key_here`
5. Run: `streamlit run app.py`

## 📚 What I Learned
Building this project helped me understand LLM API integration, secure secrets management, and end-to-end deployment (local → GitHub → Streamlit Cloud).

## 👤 Author
Sruthi Kokkirala – [LinkedIn](https://www.linkedin.com/in/sruthi-kokkirala) | [GitHub](https://github.com/sruthi-k214)
