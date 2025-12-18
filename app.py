# 🧠 LangGraph Chatbot with SQLite Persistence

LangGraph Chatbot is a **stateful AI chatbot** built with **LangGraph**, **LangChain**, and **Groq**.  
It leverages a **graph-based architecture** to manage conversation flows and persists chat history using **SQLite**, ensuring that your conversations are saved across sessions.

## 🚀 Features

*   **Graph-Based Flow:** Nodes and edges define conversation paths from start to end.
    
*   **Persistent Storage:** All chat threads and messages are saved in SQLite.
    
*   **Multi-Threaded Chat:** Switch between multiple conversation threads seamlessly.
    
*   **Streamlit UI:** Interactive, real-time web interface.
    
*   **Groq LLM Integration:** Uses `ChatGroq` for AI-generated responses.
    
*   **Environment Variable Support:** Secure API key management via `.env`.
    

## 💻 Installation

1.  Install all dependencies from `requirements.txt`:
    

`pip install -r requirements.txt`

2.  Create a `.env` file in the project root and add your Groq API key:
    

`GROQ_API_KEY=your_groq_api_key_here`

## 🛠️ Usage

Run the Streamlit app:

`streamlit run app.py`

### Features in the UI

*   **New Chat:** Start a fresh conversation.
    
*   **Thread Navigation:** Switch between existing chat threads in the sidebar.
    
*   **Real-Time Responses:** AI responses stream live as you type.
    
*   **Conversation History:** View past messages, preserved across sessions.
    

## 📁 Project Structure

`├─ app.py                  # Streamlit frontend interface ├─ langgraph_backend.py    # Chatbot backend logic and graph setup ├─ utils.py                # Utility functions (e.g., generate_thread_id) ├─ chatbot.db              # SQLite database for chat history ├─ .env                    # Environment variables (API keys) └─ requirements.txt        # Python dependencies`

## 🔧 Core Components

### Backend

*   **LangGraph StateGraph:** Manages the nodes (`chat_node`) and edges (START → chat\_node → END) for conversation flow.
    
*   **Checkpoints:** `SqliteSaver` persists all conversation states.
    
*   **Groq LLM:** Generates AI responses using `ChatGroq` and the configured API key.
    
*   **TypedDict State:** Tracks messages for each thread.
    

### Frontend

*   **Streamlit Interface:** Displays chat history, handles multiple threads, and streams AI responses in real-time.
    
*   **Sidebar Controls:** Start new chats and navigate between threads.
    
*   **Chat Input:** Users can type messages and interact with the AI seamlessly.
    

##