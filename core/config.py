import os
import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent # points to tedrec
ENV_PATH = BASE_DIR/".env" 

dotenv.load_dotenv(ENV_PATH) # reads .env file and pushes values into environment (os.environ)

DB_PATH = os.getenv("TEDREC_DB", str(BASE_DIR/"tedrec.db"))
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
TED_CHANNEL_ID = os.getenv("TED_CHANNEL_ID")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY is missing in the .env file. Kindly set it.")