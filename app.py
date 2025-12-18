#Import all the required moduels
import streamlit as st
from langgrah_backend import chatbot,retrieve_all_threads
from langchain_core.messages import HumanMessage
from IPython.display import Markdown
from utils import generate_thread_id

#Title of our streamlit app
st.title('Chatbot')

#Create all the keys in session_state to store the states while recomposition of UI

#Chat_history contains all the conversation history of the current thread
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

#This stores the current thread_id 
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

#This contains all the thread_id retrieved from sqlite databse
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()

#This function creates new thread_id and adds it to chat_threads
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

#Used to create new config dictionary with different thread_id for every new convesation
def get_config():
    return {'configurable': {'thread_id': st.session_state['thread_id']}}




#This function is used to reset the chat and start with new chat history
def reset_chat():
    new_thread_id = generate_thread_id()
    add_thread(new_thread_id)
    st.session_state['thread_id'] = new_thread_id
    st.session_state['chat_history'] = []


#Load the conversation history using thread_id 
def load_conversation(thread_id): 
    messages =  chatbot.get_state({'configurable':{'thread_id':thread_id}}).values['messages']
    temp_messages =[]
    for msg in messages:
        if isinstance(msg,HumanMessage):
            temp_messages.append({'role':'user','content':msg.content})
        else:
            temp_messages.append({'role':'ai','content':msg.content})
    return temp_messages



st.sidebar.title('LangGraph Chatbot')
#On every click it creates new thread_id with new chat
if st.sidebar.button('New Chat'):
    reset_chat()
    

st.sidebar.header('My Conversation')

#Displays all the thread_ids to load the previous conversation history by clicking on it
for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id), key=f"thread_{thread_id}"):

        st.session_state['thread_id'] = thread_id
        st.session_state['chat_history'] = load_conversation(thread_id)


    

#Take the input from user
user_input = st.chat_input('Type Here')



#Display all the conversation messages
for message in st.session_state['chat_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
    
#This part of code is used to handle the chat with user
if user_input:

    st.session_state['chat_history'].append({'role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)
    
    with st.chat_message('ai'):
    
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {
                    'messages' : [HumanMessage(content=user_input)]
                },
                config=get_config(),
                stream_mode='messages'

            )
        )
        st.session_state['chat_history'].append({'role':'ai','content':ai_message})













