import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import PyPDF2 as pdf
import requests
load_dotenv() ##load all our enviornment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text
    
def input_pdf_text (uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range (len (reader.pages)):
        page=reader.pages [page]
        text+=str(page.extract_text())
    return text

#Prompt Template
input_prompt="""
Hey Act Like a skilled or very experience ATS (Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide
best assistance for improving the resumes. Assign the percentage Matching based on the JD and
the missing keywords with high accuracy
resume: {text}
description:{JD}

# I want the response in one single string having the structure
# {{"JD Match":"%", "MissingKeywords: []", "Profile Summary":""}}

Please proved the response in one tabular format having the structure of column headers as
"JD Match":"%"
"MissingKeywords:[]"
"Profile Summary":""

"""

st.title("Application Tracking System")
# def fetch_gifs(query, limit=5):
#     api_key = "YOUR_GIPHY_API_KEY"
#     url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit={limit}"
#     response = requests.get(url)
#     data = response.json()
#     return data.get("data", [])
JD=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload your resume",type="pdf",help="Please upload the pdf")
submit=st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)
        
#C:\Program Files\Python311\python.exe\Scripts
#C:\Program Files\Python311\python.exe