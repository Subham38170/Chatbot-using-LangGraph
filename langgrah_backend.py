# import all the dependencies
from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
import sqlite3


#If database is already there then it connects otherwise creates new database with given name
conn = sqlite3.connect(database='chatbot.db',check_same_thread=False)

#Load all the enviroment variables from .env file
load_dotenv(dotenv_path=r'D:\AI ML\Gen AI\Lang_Chain\.env')  #Use the path of .env file
groq_api_key = os.environ['GROQ_API_KEY'] #Load the groq_api_key from enviroment variable

#Define llm object from Groq with groq_api_key
llm = ChatGroq(
         model='openai/gpt-oss-120b',
         api_key=groq_api_key
)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]


def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)

    return {'messages':[response]}

#Check pointer
checkPointer = SqliteSaver(conn)

#Graph which contains nodes and edges represents flow of state from one state to another to the end node
graph = StateGraph(ChatState)
graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot =graph.compile(checkpointer=checkPointer)



def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkPointer.list(None):#Here none means i want all data not particualar one
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    
    return list(all_threads)




