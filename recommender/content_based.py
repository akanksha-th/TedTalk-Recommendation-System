from embeddings import Embedder, VectorStore
from core import EMBED_MODEL

class Recommender:
    def __init__(self, model_name: str = EMBED_MODEL):
        self.embedder = Embedder(model_name)
        self.store = VectorStore(model_name)
        self.store.load()

    def recommend(self, query: str, top_k: int = 5):
        query_vec = self.embedder.embed(query)
        results = self.store.search(query_vec, top_k=top_k)
        return results