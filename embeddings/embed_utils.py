import numpy as np
from core import get_conn, save_embeddings, EMBED_MODEL
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(EMBED_MODEL)

def get_text_to_embed(video: dict) -> str:
    title = video.get("title", "")
    desc = video.get("description", "")
    return f"{title}\n\n{desc}"

def fetch_unembedded_videos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
                SELECT v.video_id, v.title, v.description
                FROM videos v
                LEFT JOIN embeddings e
                ON v.video_id = e.video_id and e.model_name=?
                WHERE e.video_id IS NULL
                """, (EMBED_MODEL,))
    rows = cur.fetchall()
    conn.close()

    return [{"video_id": r[0], "title": r[1], "description": r[2]} for r in rows]

def embed_and_store():
    videos = fetch_unembedded_videos()
    print(f"Found {len(videos)} videos needing embeddings")

    for v in videos:
        text = get_text_to_embed(v)
        vec = model.encode(text, convert_to_numpy=True, normalize_embeddings=True).astype("float32")

        save_embeddings(v["video_id"], EMBED_MODEL, vec)
        print(f"Embedded {v['video_id']} ({v['title'][:40]}...)")

if __name__ == "__main__":
    embed_and_store()