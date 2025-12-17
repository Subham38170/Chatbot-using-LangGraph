import streamlit as st
from langgrah_backend import chatbot
from langchain_core.messages import HumanMessage
from IPython.display import Markdown


CONFIG = {'configurable':{'thread_id':1}}

st.title('Chatbot')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

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
                config=CONFIG,
                stream_mode='messages'

            )
        )
        st.session_state['chat_history'].append({'role':'ai','content':ai_message})













