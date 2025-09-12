from googleapiclient.discovery import build
from core import YOUTUBE_API_KEY, TED_CHANNEL_ID

"""
Run in the main directory, as a module:
python -m test_scripts.test_yt_api
"""

def test_yt():
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelId=TED_CHANNEL_ID,
        maxResults=3,
        order="date"
    )
    response = request.execute()
    for item in response.get("items", []):
        print("Video Id: ", item['id'].get('videoId'))
        print("Title: ", item['snippet'].get('title'))
        print("----")

if __name__ == "__main__":
    test_yt()