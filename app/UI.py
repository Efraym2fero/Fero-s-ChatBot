import streamlit as st 
from streamlit_chat import message
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage





class ChatUI :
    def __init__(self,model="mistral-small-2506",temperature = 0 , API_KEY =st.secrets["MISTRAL_API_KEY"]):
        self.llm = ChatMistralAI(model = model,temperature=temperature,api_key= API_KEY)

    def pageConfig(self,title = "Fero's chatbot",icon="🤖",header = "Fero's chatbot 🤖"):
        st.set_page_config(
            page_title = title,
            page_icon = icon)
        st.header(header)

    def chatForm(self):
            chat_container = st.container()
            if "messages" not in st.session_state:
                st.session_state.messages= [
                    SystemMessage(content = "You are Fero a helpful asssistant made by AI Engineer Efraym Emad (افرايم عماد))")
                ]
            with st.form("my_form", clear_on_submit=True):
                user_text = st.text_input("Enter something:")
                submitted = st.form_submit_button("Submit")

            if submitted and user_text:
                st.session_state.messages.append(HumanMessage(content = user_text))
                with st.spinner("🤖 Thinking..."):
                    modelResponse = self.llm.invoke(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content = modelResponse.content))

            return st.session_state.get("messages",[]),chat_container

    def chatContainer(self,messages,chat_container):

        with chat_container:
            for i , msg in enumerate(messages):
                if isinstance(msg,SystemMessage):
                        continue
                        
                if isinstance(msg, HumanMessage):    
                    message(msg.content, is_user =True,key = str(i)+ 'User',avatar_style="fun-emoji",seed ="farfor")
                        
                elif isinstance(msg, AIMessage):
                    message(msg.content, is_user =False,key = str(i)+ 'AI',avatar_style="bottts",seed="blue bot")
