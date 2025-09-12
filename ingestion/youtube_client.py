from googleapiclient.discovery import build
from core import YOUTUBE_API_KEY, TED_CHANNEL_ID

class YouTubeClient:
    def __init__(self, api_key: str = None):
        api_key = api_key or YOUTUBE_API_KEY
        if not api_key:
            raise ValueError("Missing YOUTUBE API KEY")
        self.youtube = build("youtube", "v3", developerKey=api_key)
        self.channel_id = TED_CHANNEL_ID

    def get_uploads_playlist_id(self) -> str:
        response = self.youtube.channels().list(
            part="ContentDetails",
            id=self.channel_id
        ).execute()
        return response['items'][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    def fetch_playlist_videos(self, playlist_id: str, max_pages: int = None):
        """Fetch videos from a playlist, handling pagination."""
        videos = []
        page_token = None
        pages = 0

        while True:
            request = self.youtube.playlistItems().list(
                part="snippet,contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=page_token
            )
            response = request.execute()

            for item in response.get("items", []):
                snippet = item["snippet"]
                video_id = item["contentDetails"]["videoId"]
                videos.append({
                    "video_id": video_id,
                    "title": snippet.get("title", ""),
                    "description": snippet.get("description", ""),
                    "channel_id": snippet.get("channelId", ""),
                    "channel_title": snippet.get("channelTitle", ""),
                    "published_at": snippet.get("publishedAt", ""),
                    "thumbnail_url": snippet["thumbnails"].get("high", {}).get("url", "")
                })

            page_token = response.get("nextPageToken")
            pages += 1
            if not page_token or (max_pages and pages >= max_pages):
                break

        return videos