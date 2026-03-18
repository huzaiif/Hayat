import os
import streamlit as st
from dotenv import load_dotenv

def get_google_api_key():
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY")

def load_css():
    css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "styles.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
