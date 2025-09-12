from core import init_db, add_videos
from .youtube_client import YouTubeClient

def update_ted_videos(max_pages=5):
    """Fetch TED channel videos and insert/update DB."""
    init_db()
    client = YouTubeClient()
    uploads_id = client.get_uploads_playlist_id()
    print("Uploads playlist ID:", uploads_id)

    videos = client.fetch_playlist_videos(uploads_id, max_pages=max_pages)
    print(f"Fetched {len(videos)} videos")

    add_videos(videos)
    print("Inserted into DB")

if __name__ == "__main__":
    update_ted_videos(max_pages=5)