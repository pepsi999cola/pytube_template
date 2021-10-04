from pytube import Playlist

url = input('URLを入力してください:')
p = Playlist(url)

print(f'Downloading: {p.title}')
print(p.length)

for video in p.videos:
    (video.streams
    .filter(progressive=True, file_extension='mp4')
    .desc()
    .order_by('resolution')
    .first()
    .download()
    )
    print(video.title)