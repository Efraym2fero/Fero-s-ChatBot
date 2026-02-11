import streamlit as st 
from streamlit_chat import message
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")
model = "mistral-small-2506"


def pageConfig(title = "Fero's chatbot",icon="🤖",header = "Fero's chatbot 🤖"):
    st.set_page_config(
        page_title = title,
        page_icon = icon)
    st.header(header)
