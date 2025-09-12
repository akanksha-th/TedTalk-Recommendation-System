from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
print("Looking for .env at:", env_path)
loaded = load_dotenv(env_path)
print("Loaded:", loaded)
print("YOUTUBE_API_KEY:", os.getenv("YOUTUBE_API_KEY"))