from pytube import Channel

# channel_urlを入力
url = input('YoutubechannelのURLを入力してください:')
c = Channel(url)

print(f'Downloading videos by: {c.channel_name}')
print(c.length)

for video in c.videos:
    (video.streams
        .get_highest_resolution()
        .download()
    )
    print(video.title)
