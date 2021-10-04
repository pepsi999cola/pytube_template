from pytube import Playlist

url = input('URLを入力してください:')
p = Playlist(url)

print(f'Downloading: {p.title}')
print(p.length)

for video in p.videos:
    (video.streams
        .get_highest_resolution()
        .download()
    )
    print(video.title)