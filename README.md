## Project Structure

    tedrec/
    ├── app.py                  # Streamlit entrypoint
    ├── requirements.txt
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



## How did I go by it?
database+ingestion -> embeddings -> streamlit ui mvp -> further advancements
