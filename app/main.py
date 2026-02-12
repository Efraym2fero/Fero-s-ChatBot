import streamlit as st 
from streamlit_chat import message
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from UI import ChatUI




if __name__ == "__main__":
    chatUi = ChatUI()

    
    chatUi.pageConfig() 


    messages,chatContainer = chatUi.chatForm()

    chatUi.chatContainer(messages,chatContainer)
   


    
