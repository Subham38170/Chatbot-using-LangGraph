#   

# 🧠 LangGraph Chatbot with SQLite Persistence

# 

A production-ready **stateful AI agent** built with **LangGraph**, **LangChain**, and **Groq**. This chatbot uses a **graph-based state machine** to manage conversation flows and integrates **SQLite** to ensure long-term memory across sessions.

* * *

## 📖 What is this Chatbot?

# 

Unlike traditional chatbots that simply send a prompt and get a response, this bot is built on a **directed acyclic graph (DAG)** logic. It treats every conversation as a "state" that can be saved, modified, and resumed.

### How it "Thinks" (The Graph)

# 

The bot operates through a series of **Nodes** and **Edges**:

*   **Nodes:** Functions that process data (e.g., the `chat_node` calls the LLM).
    
*   **Edges:** The "roads" that connect nodes (e.g., moving from the user input to the AI response).
    
*   **State:** A shared memory that travels through the graph, holding the conversation history.
    

* * *

## ✨ Key Features

# 

*   **🔁 Persistent Memory:** Uses `SqliteSaver` to store chat history permanently on your disk.
    
*   **🧵 Multi-Threaded Support:** Manage different conversations simultaneously using unique `thread_ids`.
    
*   **⚡ Groq Inference:** Powered by Groq's LPU for ultra-fast, near-instant AI responses.
    
*   **🎨 Streamlit UI:** A clean, interactive web interface with real-time response streaming.
    
*   **🔄 History Retrieval:** Even if the server restarts, your chat history remains intact.
    

* * *

## 🏗️ Architecture

# 

The system is divided into two main layers:

### 1\. The Backend (LangGraph)

# 

The backend defines the **State Schema**. It uses a `TypedDict` and the `add_messages` annotator. This is the secret sauce: instead of replacing the old message with a new one, it intelligently **appends** to the list, maintaining context.

### 2\. The Persistence Layer (SQLite)

# 

Every time the chatbot speaks, a "checkpoint" is saved.

*   **Database:** `chatbot.db`
    
*   **Key:** `thread_id` (used to distinguish between different users or topics).
    

* * *

## 🚀 Getting Started

### 📦 Installation

# Bash

    # Clone the repository
    git clone https://github.com/your-username/langgraph-sqlite-chatbot.git
    cd langgraph-sqlite-chatbot
    
    # Install dependencies
    pip install -r requirements.txt

### 🔑 Configuration

# 

Create a `.env` file in the root directory:

Plaintext

    GROQ_API_KEY=your_groq_api_key_here

### 🛠️ Running the App

# Bash

    streamlit run app.py

* * *

## 📁 Project Structure

# Plaintext

    ├─ app.py                # Streamlit UI & Frontend logic
    ├─ langgraph_backend.py  # Graph definition & LLM setup
    ├─ utils.py              # Helper functions (Thread ID generation)
    ├─ chatbot.db            # SQLite database (Auto-generated)
    ├─ .env                  # Environment secrets
    └─ requirements.txt      # Python dependencies

* * *

## 📌 Use Cases

# 

*   **Customer Support:** Remember user issues across multiple days.
    
*   **Personal Mentors:** Build an AI that remembers your learning progress.
    
*   **Agent Workflows:** A base for more complex agents that need to "pause" and "resume" tasks.