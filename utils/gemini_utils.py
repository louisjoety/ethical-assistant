import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get the Gemini API key
api_key = st.secrets["GEMINI_API_KEY"]
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_gemini_summary(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
