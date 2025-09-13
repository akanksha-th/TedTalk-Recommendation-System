import os
import dotenv
import streamlit as st
from pathlib import Path

try:
    secrets = st.secrets
except ImportError:
    secrets = {}

BASE_DIR = Path(__file__).resolve().parent.parent # points to tedrec
ENV_PATH = BASE_DIR/".env" 

dotenv.load_dotenv(ENV_PATH) # reads .env file and pushes values into environment (os.environ)

def get_var(key: str, default: str = None) -> str:
    """Check streamlit secrets then .env then defaults"""
    return secrets.get(key) or os.getenv(key, default)

DB_PATH = get_var("TEDREC_DB", str(BASE_DIR/"tedrec.db"))
EMBED_MODEL = get_var("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
YOUTUBE_API_KEY = get_var("YOUTUBE_API_KEY")
TED_CHANNEL_ID = get_var("TED_CHANNEL_ID", "UCAuUUnT6oDeKwE6v1NGQxug")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY is missing!! Kindly set it.")