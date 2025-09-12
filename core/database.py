import os
import sqlite3
import numpy as np
from pathlib import Path
from core.config import DB_PATH

# connect to db
def get_conn():
    """Returb a sqlite3 connection object (auto-creates db file)"""
    conn = sqlite3.connect(DB_PATH)
    return conn

# Schema setup
SCHEMA = """
CREATE TABLE IF NOT EXISTS videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    description TEXT,
    channel_id TEXT,
    channel_title TEXT,
    published_At TEXT,
    thumbnail_url TEXT
);

CREATE TABLE IF NOT EXISTS embeddings (
    video_id TEXT,
    model_name TEXT,
    vector BLOB,
    PRIMARY KEY(video_id, model_name),
    FOREIGN KEY(video_id) REFERENCES videos(video_id)
);
"""

def init_db():
    """"create tables if they don't exist"""
    conn = get_conn()
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()

# Insert/update videos
def add_videos(rows):
    """
    rows = list of dicts with keys:
        video_id, title, description, channel_id, channel_title,
        published_at, thumbnail_url
    """
    conn = get_conn()
    cur = conn.cursor()
    for r in rows:
        cur.execute("""
            INSERT INTO videos (video_id, title, description, channel_id, channel_title, published_at, thumbnail_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(video_id) DO UPDATE SET
                title=excluded.title,
                description=excluded.description,
                channel_id=excluded.channel_id,
                channel_title=excluded.channel_title,
                published_at=excluded.published_at,
                thumbnail_url=excluded.thumbnail_url
        """, (
            r["video_id"], r.get("title", ""), r.get("description", ""),
            r.get("channel_id", ""), r.get("channel_title", ""),
            r.get("published_at", ""), r.get("thumbnail_url", "")
        ))
    conn.commit()
    conn.close()

# add embeddings
def save_embeddings(video_id: str, model_name: str, vector: np.ndarray):
    """Save embedding as BLOB. Overwrites if already exists."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO embeddings (video_id, model_name, vector)
                VALUES (?, ?, ?)
                ON CONFLICT(video_id, model_name) DO UPDATE SET
                vector = excluded.vector
                """, (video_id, model_name, vector.astype("float32").tobytes()))
    conn.commit()
    conn.close()
    
# load embeddings
def load_embeddings(model_name: str):
    """
    Returns list of dicts: {video_id, vector}
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT video_id, vector FROM embeddings WHERE model_name=?", (model_name,))
    rows = cur.fetchall()
    conn.close()

    results = []
    for vid, blob in rows:
        vec = np.frombuffer(blob, dtype='float32')
        results.append({"video_id": vid, "vector": vec})
    return results

# Fetch metadata for recommendations
def get_video_metadata(video_ids):
    conn = get_conn()
    cur = conn.cursor()
    q_marks = ",".join("?" * len(video_ids))
    cur.execute(f"SELECT video_id, title, description, thumbnail_url, published_at FROM videos WHERE video_id IN ({q_marks})", video_ids)
    rows = cur.fetchall()
    conn.close()
    return [
        {
            "video_id": r[0],
            "title": r[1],
            "description": r[2],
            "thumbnail_url": r[3],
            "published_at": r[4]
        }
        for r in rows
    ]

if __name__ == "__main__":
    # Only runs if you do: python -m core.database
    print("Initializing DB…")
    init_db()
    print("DB initialized")