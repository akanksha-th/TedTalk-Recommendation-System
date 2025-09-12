from .embed_utils import model
import numpy as np

class Embedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Wrapper around a Hugging Face sentence-transformer model.
        Downloads if not cached locally.
        """
        self.model_name = model_name
        self.model = model

    def embed(self, text: str) -> np.ndarray:
        """
        Convert text into a normalized vector (numpy array).
        """
        if not text or not text.strip():
            raise ValueError("Input text is empty!")

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True  # ensures cosine similarity works as dot product
        )
        return embedding
