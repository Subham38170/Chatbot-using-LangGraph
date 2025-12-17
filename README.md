# LangGraph Chatbot with Persistence

This project is a stateful AI chatbot built using **LangGraph**, **LangChain**, and **Groq**. It utilizes a graph-based architecture to manage conversation flows and features a persistence layer that allows the bot to remember past interactions using unique thread IDs.

---

## 🏗️ Architecture & How It Works

This chatbot is designed as a **State Machine**. Instead of a simple linear script, it uses a directed graph to control how data moves through the system.

### 1. State Definition (`ChatState`)
The "State" is the shared memory of the graph. We use a `TypedDict` that contains a list of `messages`. By using the `add_messages` annotator, LangGraph automatically appends new messages to the existing history rather than overwriting them.

### 2. The Node (`chat_node`)
Nodes are the building blocks of the graph.
* **The Function:** The `chat_node` takes the current state, sends the message history to the Groq LLM, and receives a response.
* **The Return:** It returns the LLM's response, which is then merged back into the state.

### 3. The Workflow (Graph Construction)
The flow is defined by edges:
* **START ➔ chat_node**: When a user sends a message, it triggers the chat node.
* **chat_node ➔ END**: Once the LLM responds, the process finishes.

### 4. Persistence (`InMemorySaver`)
This is the "memory" of the chatbot.
* **Checkpointer**: We use `InMemorySaver()` to act as a checkpointer.
* **Thread IDs**: By saving the state at every step, the chatbot can resume a conversation later. As long as you provide the same `thread_id`, the bot will "remember" what was said in previous turns.



---

## 🚀 Setup and Installation

### Prerequisites
* Python 3.9+
* A Groq API Key
