import yt_dlp

def download_video(url, output_path='.'):
    ydl_opts = {
        'format': 'best',  # Choose the best quality
        # 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Prefer mp4 format
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,  # Set to False if you want to download playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=fKts5sczKEw'
    download_video(video_url)
    print("Download completed!")