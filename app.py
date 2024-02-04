import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()
from prompt import CustomPrompt

my_prompt = CustomPrompt()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def model_prediction(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text

import PyPDF2 as pdf
def read_pdf(file):
    reader = pdf.PdfReader(file)
    text=""
    for page in reader.pages:
        text += str(page.extract_text())
    return text


#Application
image = Image.open("Image/header.png")
st.set_page_config(page_title='ATS',page_icon=image)
st.title("Aplication Tracking System (ATS)")
st.text("Matching Your Resume")
job_description = st.text_area("Please Provide the Job Description",
                               height=300)
upload_file = st.file_uploader("Please Upload Your Resume", 
                               type="pdf")
submit = st.button("Submit")

if submit:
    if upload_file:
        text = read_pdf(upload_file)
        response = model_prediction(my_prompt.prompt_text)
        st.text(response)
    else:
        st.text("Please Upload PDF")