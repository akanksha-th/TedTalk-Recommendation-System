import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Load .env for local dev
load_dotenv(ENV_PATH)

# Try to import Streamlit secrets safely
secrets = {}
try:
    import streamlit as st
    if hasattr(st, "secrets"):
        secrets = st.secrets
except Exception:
    secrets = {}

def get_var(key: str, default: str = None) -> str:
    """Check Streamlit secrets → environment → default"""
    if key in secrets:
        return secrets[key]
    return os.getenv(key, default)

DB_PATH = get_var("TEDREC_DB", str(BASE_DIR / "tedrec.db"))
EMBED_MODEL = get_var("EMBED_MODEL", "all-MiniLM-L6-v2")
YOUTUBE_API_KEY = get_var("YOUTUBE_API_KEY")
TED_CHANNEL_ID = get_var("TED_CHANNEL_ID", "UCAuUUnT6oDeKwE6v1NGQxug")

if not YOUTUBE_API_KEY:
    raise ValueError(
        "YOUTUBE_API_KEY is missing!! Kindly set it."
    )

if __name__ == "__main__":
    print("DEBUG YOUTUBE_API_KEY:", bool(YOUTUBE_API_KEY))
    print("DEBUG EMBED_MODEL:", EMBED_MODEL)
    print("DEBUG TED_CHANNEL_ID:", TED_CHANNEL_ID)
    print("DEBUG DB_PATH:", DB_PATH)
