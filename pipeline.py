# pipeline.py
from ingestion import update_ted_videos
from embeddings import embed_and_store
from recommender import Recommender

def run_pipeline(query: str, top_k: int = 5):
    print("=== STEP 1: Updating TED videos ===")
    update_ted_videos(max_pages=10)  # set limit or remove for full fetch

    print("=== STEP 2: Embedding videos ===")
    embed_and_store()

    print("=== STEP 3: Running recommendation ===")
    rec = Recommender()
    results = rec.recommend(query, top_k=top_k)

    print("\nTop Recommendations:")
    for r in results:
        print(f"- {r['title']} ({r['score']:.3f})")

if __name__ == "__main__":
    run_pipeline("Talks about artificial intelligence and future of work", top_k=5)
