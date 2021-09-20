from pytube import Channel

c = Channel('https://www.youtube.com/channel/')  # channel_urlを入力
print(f'Downloading videos by: {c.channel_name}')
for video in c.videos:
    video.streams.filter(progressive=True, file_extension='mp4').desc().order_by(
        'resolution').first().download()
    print(video.title)
