from pytube import Playlist

url = input('URLを入力してください:')
p = Playlist(url)

print(f'Downloading: {p.title}')
print(f'動画数{p.length}')
print(f'トータル視聴回数{p.views}')

for video in p.videos:
    print(video.title)