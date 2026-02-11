import streamlit as st 
from streamlit_chat import message
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from UI import pageConfig



load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")
model = "mistral-small-2506"



if __name__ == "__main__":

    llm = ChatMistralAI(model = model,temperature=0,api_key= API_KEY) 
    pageConfig()    
    if "messages" not in st.session_state:
        st.session_state.messages= [
            SystemMessage(content = "You are Fero a helpful asssistant made by AI Engineer Efraym Emad (افرايم عماد))")
        ]

    chat_container = st.container()

    with st.form("my_form", clear_on_submit=True):
        user_text = st.text_input("Enter something:")
        submitted = st.form_submit_button("Submit")

    if submitted and user_text:
        st.session_state.messages.append(HumanMessage(content = user_text))
        with st.spinner("🤖 Thinking..."):
            modelResponse = llm.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content = modelResponse.content))

    messages = st.session_state.get("messages",[])

    with chat_container:
        for i , msg in enumerate(messages):
            if isinstance(msg,SystemMessage):
                    continue
                    
            if isinstance(msg, HumanMessage):    
                message(msg.content, is_user =True,key = str(i)+ 'User',avatar_style="fun-emoji",seed = "farfor")
                    
            else:
                message(msg.content, is_user =False,key = str(i)+ 'AI',avatar_style="bottts",seed="blue bot")
    