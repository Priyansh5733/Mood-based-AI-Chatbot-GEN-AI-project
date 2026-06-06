
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Page Config
st.set_page_config(
    page_title="Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Model
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

# Header
st.title("🤖 Mood Based AI Chatbot")
st.markdown("Choose a mood and start chatting with your AI assistant.")

# Mood Selection
mood = st.selectbox(
    "Select Chatbot Mood",
    ["Funny", "Sad", "Angry"]
)

# Initialize Messages
if "messages" not in st.session_state or st.session_state.get("current_mood") != mood:

    st.session_state.current_mood = mood

    if mood == "Funny":
        system_message = SystemMessage(
            content="You are a funny AI Agent."
        )

    elif mood == "Sad":
        system_message = SystemMessage(
            content="You are a sad AI Agent and answer in a sad way."
        )

    else:
        system_message = SystemMessage(
            content="You are an angry AI Agent."
        )

    st.session_state.messages = [system_message]

# Display Chat History
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# User Input
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.rerun()

