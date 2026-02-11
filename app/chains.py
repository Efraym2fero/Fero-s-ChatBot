from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain.schema import {SystemMessage,HumanMessage,AIMessage}


load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")
model = "mistral-small-2506"

def chat(model = model , temperature= 0, api = API_KEY):
    llm = ChatMistralAI(model = model,temperature=temperature,api_key= api) 
    return llm

