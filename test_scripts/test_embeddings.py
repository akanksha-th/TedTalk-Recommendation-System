from embeddings import Embedder

embedder = Embedder("all-MiniLM-L6-v2")

vec = embedder.embed("Talks about climate change and sustainability")
print(vec.shape)   # (384,)
print(vec[:5])     # first 5 values of vector
