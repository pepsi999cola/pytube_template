import os
from pytube import Playlist

url = input('URLを入力してください:')
p = Playlist(url)

print(f'Downloading: {p.title}')
print(p.length)
os.makedirs(p.title, exist_ok=True)

for video in p.videos:
    (video.streams
        .get_highest_resolution()
        .download(p.title)
    )
    print(video.title)