import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage

from src.LanggraphagenticAI.UI.uiconfig import Config     

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}
    
    def initialize_session(self):
        return {
            "current_step" :"requirements",
            "requirements" :"",
            "user_storeis": "",
            "PO feedback" : "",
            "generated code": "",
            "review feedback" :"",
            "decision" : None
        }

    def render_requirements(self):
        st.markdown("### Requirements submission")
        st.session_state.state["Requirements"]=st.text_area("Enter your requriements:",height=200,key="req_input")

        if st.button("Submit Requirements", key="submit_req"):
            st.session_state.state["Current step"]="Generate User Stories"
            st.session_state.state.IsSDLC= True


    def load_streamlit_ui(self):
        st.set_page_config(page_title="" + self.config.get_page_title(),layout= "wide")
        st.header(" " + self.config.get_page_title())
        st.session_state.timeframe=''
        st.session_state.IsFetchButtonClicked=False
        st.session_state.IsSDLC=False


        with st.sidebar:
            #Get LLM options from Config
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            #LLM Selection
            self.user_controls["selected_llm"]=st.selectbox("Select llm", llm_options)
             
            if self.user_controls["selected_llm"] =="Groq":
                # Model selection 
                model_options=self.config.get_groq_model_options()
                self.user_controls["selected_Groq_Model"]=st.selectbox("Selected Model", model_options)

                #API Key input
                self.user_controls["GROQ_API_KEY"]=st.session_state["GRQO_API_KEY"]=st.text_input("API Key ", type ="password")

                #validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter the correct GROQ API key to proceed further, Dont have one please refer to GROQ wesbite and create one")
            
             #Usecase Selection
            self.user_controls["selected_usecases"]=st.selectbox("Select usecases",usecase_options)
            
            if "state" not in st.session_state:
                st.session_state.state=self.initialize_session()
            self.render_requirements()
        return self.user_controls
            