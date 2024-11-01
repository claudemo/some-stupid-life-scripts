#!/usr/bin/env python3

import sys
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    """
    regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        print('Error: Could not extract video ID from the URL.')
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print('Usage: python script.py <YouTube URL>')
        sys.exit(1)

    url = sys.argv[1]
    video_id = extract_video_id(url)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f'Error fetching transcript: {e}')
        sys.exit(1)

    folder = 'youtube-transcript'
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, f'{video_id}.txt')

    # Combine all the transcript texts
    transcript_text = ' '.join([t['text'] for t in transcript])

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(transcript_text)

    print(f'Transcript saved to {filename}')

if __name__ == '__main__':
    main()