from dotenv import load_dotenv
import os
import textwrap
load_dotenv()
import streamlit as st
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(question):
    response=model.generate_content(question)
    return (response.text)


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input" )
submit=st.button("Get Response")

if submit:
    response=get_gemini_response(input)
    st.subheader("The Respose is")
    st.write(response)