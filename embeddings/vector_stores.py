import numpy as np
from core import load_embeddings, get_video_metadata
from sentence_transformers import util
from core import EMBED_MODEL

class VectorStore:
    def __init__(self, model_name: str = EMBED_MODEL):
        self.model_name = model_name
        self.embeddings = None
    
    def load(self):
        self.embeddings = load_embeddings(self.model_name)
        print(f"Loaded {len(self.embeddings)} embeddings from DB.")

    def search(self, query_vec: np.ndarray, top_k: int = 5):
        if self.embeddings is None:
            self.load()

        # stack all vectors into numpy array
        ids = [emb["video_id"] for emb in self.embeddings]
        mat = np.vstack([emb["vector"] for emb in self.embeddings])

        # cosine similarity
        scores = util.cos_sim(query_vec, mat)[0].cpu().numpy()

        # top k indices
        top_idx = np.argsort(scores)[::-1][:top_k]
        top_ids = [ids[i] for i in top_idx]
        top_scores = [scores[i] for i in top_idx]

        metadata = get_video_metadata(top_ids)
        for m, s in zip(metadata, top_scores):
            m["score"] = float(s)
        return metadata