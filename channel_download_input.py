import os
from pytube import Channel

# channel_urlを入力
url = input('YoutubechannelのURLを入力してください:')
c = Channel(url)

print(f'Downloading videos by: {c.channel_name}')
os.makedirs(c.channel_name, exist_ok=True)

for video in c.videos:
    (video.streams
        .get_highest_resolution()
        .download(c.channel_name)
    )
    print(video.title)
