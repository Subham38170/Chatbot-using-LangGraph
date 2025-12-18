import streamlit as st
from langgrah_backend import chatbot,retrieve_all_threads
from langchain_core.messages import HumanMessage
from IPython.display import Markdown
from utils import generate_thread_id


st.title('Chatbot')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def get_config():
    return {'configurable': {'thread_id': st.session_state['thread_id']}}




#This functio is used to reset the chat and start with new chat history
def reset_chat():
    new_thread_id = generate_thread_id()
    add_thread(new_thread_id)
    st.session_state['thread_id'] = new_thread_id
    st.session_state['chat_history'] = []


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
if st.sidebar.button('New Chat'):
    reset_chat()
    

st.sidebar.header('My Conversation')

for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id), key=f"thread_{thread_id}"):

        st.session_state['thread_id'] = thread_id
        st.session_state['chat_history'] = load_conversation(thread_id)


    


user_input = st.chat_input('Type Here')



#Loading the conversational history
for message in st.session_state['chat_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
    

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













