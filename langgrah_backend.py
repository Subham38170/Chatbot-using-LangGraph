# Import necessary dependencies
from langgraph.graph import StateGraph, START, END  
from typing import TypedDict, Annotated  
from langchain_core.messages import BaseMessage, HumanMessage 
from langchain_groq import ChatGroq  
from langgraph.checkpoint.memory import InMemorySaver  
from langgraph.checkpoint.sqlite import SqliteSaver  
from langgraph.graph.message import add_messages  
from dotenv import load_dotenv  
import os  
import sqlite3  

# Connect to SQLite database with name chatbot.db if it doesn't exists then it creates new one with given name
# check_same_thread=False allows SQLite to be used across multiple threads
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)

# Load environment variables from .env file
load_dotenv(dotenv_path=r'D:\AI ML\Gen AI\Lang_Chain\.env')  # Specify path to your .env file

# Retrieve the Groq API key from environment variables
groq_api_key = os.environ['GROQ_API_KEY']

# Initialize the ChatGroq LLM with the API key and model name
llm = ChatGroq(
    model='openai/gpt-oss-120b',  
    api_key=groq_api_key          
)

# Define the state structure for the chatbot
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]  # Annotated to auto-add messages

# Define a node in the graph to handle chat logic
def chat_node(state: ChatState):
    messages = state['messages']           #
    response = llm.invoke(messages)       
    return {'messages': [response]}       

# Initialize a checkpoint pointer using SQLite for persistence
checkPointer = SqliteSaver(conn)

# Create the state graph representing the chatbot flow
graph = StateGraph(ChatState)

# Add a node to the graph
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# Compile the graph into a chatbot object with persistence
chatbot = graph.compile(checkpointer=checkPointer)

# Function to retrieve all saved conversation threads from the database
def retrieve_all_threads():
    all_threads = set()  # Use a set to avoid duplicates
    for checkpoint in checkPointer.list(None):  # None retrieves all saved checkpoints
        all_threads.add(checkpoint.config['configurable']['thread_id'])  # Extract thread IDs
    return list(all_threads)  
