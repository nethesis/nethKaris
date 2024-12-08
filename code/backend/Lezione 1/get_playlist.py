import scrapetube

def get_video_url_from_playlist(playlist_url):
    # Extract the playlist ID from the URL
    playlist_id = playlist_url.replace("https://www.youtube.com/playlist?list=", "")
    
    # Get a list of videos in the playlist
    videos = scrapetube.get_playlist(playlist_id=playlist_id)
    
    # Create a list to hold video URLs
    video_urls = []
    
    # Iterate over the videos and construct the URLs
    for video in videos:
        video_id = video['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_urls.append(video_url)
    
    return video_urls

# Example usage
#playlist_url = "https://www.youtube.com/playlist?list=PLWzKfs3icbT6yhDTpO1GyDlz9AXdWSiGr"
#print(get_video_url_from_playlist(playlist_url))
