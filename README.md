# 🤖 Mood-Based AI Chatbot

A simple and interactive AI chatbot built using **Python**, **Streamlit**, **LangChain**, and **Mistral AI**. The chatbot allows users to choose different moods and interact with AI personalities in real time.

## ✨ Features

* 🎭 Multiple chatbot personalities:

  * Funny
  * Sad
  * Angry
* 💬 Interactive chat interface using Streamlit
* 🧠 Conversation memory using LangChain message history
* ⚡ Powered by Mistral AI
* 🎨 Clean and user-friendly UI

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* Python Dotenv

## 📂 Project Structure

```text
project/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root and add:

```env
MISTRAL_API_KEY=your_api_key_here
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

## 🎭 Available Chatbot Moods

### 😂 Funny Mode

Responds with humor and light-hearted answers.

### 😢 Sad Mode

Responds in a sad and emotional tone.

### 😡 Angry Mode

Responds in an angry and aggressive tone.

## 📸 Demo

Choose a mood from the dropdown menu and start chatting with the AI assistant.

## 🎯 Learning Objectives

This project demonstrates:

* LangChain message handling
* SystemMessage, HumanMessage, and AIMessage
* Mistral AI integration
* Streamlit UI development
* Stateful chatbot conversations

## 📜 License

This project is open source and available under the MIT License.
