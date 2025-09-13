# TedTalk-Recommendation-System
This project is a recommendation system for TED Talks built with Flask. It connects to the YouTube Data API to fetch TED videos, stores them in a SQLite database and generates embeddings using open-source HuggingFace models.Recommendations are made through content-based filtering, matching user queries to the most relevant TED Talks. 

The project provides both:
- a **Streamlit prototype** for local experimentation, and  
- a **Flask-based web UI** deployed on **Render** for easy usage.  

---

## Project Structure

    tedrec/
    ├── run_locally.py          # Streamlit entrypoint
    ├── requirements.txt
    ├── Procfile                # Deployment entrypoint
    ├── pipeline.py
    ├── tedrec.db
    ├── .env                    # holds YOUTUBE_API_KEY, DB path, etc.
    │
    ├── core/
    │   ├── __init__.py
    │   ├── config.py           # loads env vars, constants
    │   ├── database.py         # DB connection + migrations
    │   ├── models.py           # ORM-style dataclasses or SQLAlchemy models
    │
    ├── ingestion/
    │   ├── __init__.py
    │   ├── youtube_client.py   # wraps YouTube Data API
    │   ├── updater.py          # pulls new videos, upserts into DB
    │
    ├── embeddings/
    │   ├── __init__.py
    │   ├── embedder.py         # class Embedder -> build, encode, persist
    │   ├── vector_store.py     # class VectorStore -> search 
    │   ├── embed_utils.py     
    │
    ├── recommender/
    │   ├── __init__.py
    │   ├── content_based.py    # ContentRecommender
    │
    ├── ui/
    │   ├── __init__.py
    │   ├── flask_app.py        # Flask web UI
    |   ├── templates/
    |      ├── index.html 

---

## Development Flow

1. Build database + ingestion layer  
2. Add embeddings + vector search  
3. Prototype with Streamlit UI (MVP)  
4. Extend with Flask-based web UI  
5. Deploy on Render

---

## Getting Started

**Clone the repo**
```bash
git clone <the-repo-url>
cd tedrec
```

**Create virtual environment and install dependencies**
```bash
python -m venv tedrec
tedrec\Scripts\activate # On Windows
# or: source tedrec/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

**Set environment variables (.env)**
```bash
YOUTUBE_API_KEY=your_youtube_api_key_here
EMBED_MODEL=all-MiniLM-L6-v2
TED_CHANNEL_ID=UCAuUUnT6oDeKwE6v1NGQxug
TEDREC_DB=tedrec.db
```

**Run the pipeline and launch the interactive UI**
```bash
python pipeline.py
```

**Run locally**
```bash
# Option 1: Streamlit prototype
streamlit run run_locally.py

# Option 2: Flask app
python -m ui.flask_app
```
