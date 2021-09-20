from pytube import Channel

# channel_urlを入力
c = Channel('https://www.youtube.com/channel/UCfvZempyFTpPlklLojBj0iQ/videos')

print(f'Downloading videos by: {c.channel_name}')
for video in c.videos:
    (video.streams
          .filter(progressive=True, file_extension='mp4')
          .desc()
          .order_by('resolution')
          .first()
          .download()
     )
    print(video.title)
