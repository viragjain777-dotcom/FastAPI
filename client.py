import os
from dotenv import load_dotenv
import streamlit as st
import requests


def get_openai_response(user_input):
    response=requests.post("http://localhost:8000/essay/invoke", json={'input':{"topic": user_input}})
    return response.json()['output']['content']

def get_ollama_response(user_input1):
    response=requests.post("http://localhost:8000/poem/invoke", json={'input':{"topic": user_input1}})
    return response.json()['output']

    ## streamlit FW

st.title("Langchain FastAPI App")
user_input=st.text_input("Enter your essay question here:")
user_input1=st.text_input("Enter your poem question here:")

if user_input:
    st.write(get_openai_response(user_input))

if user_input1:
    st.write(get_ollama_response(user_input1))