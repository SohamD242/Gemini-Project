from dotenv import load_dotenv
import os
import textwrap
load_dotenv()
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input" )
   
st.markdown("<div class='upload-container'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
st.markdown("</div>", unsafe_allow_html=True)

# Display the uploaded image
if uploaded_file is not None:
    st.markdown("<div class='image-container'>", unsafe_allow_html=True)
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='image-container'><p>No image uploaded yet.</p></div>", unsafe_allow_html=True)


submit=st.button("Tell me abot the image")

response=get_gemini_response(input,image)

st.subheader("The Response is")
st.write(response.text)

