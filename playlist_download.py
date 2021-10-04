from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
print(f'Downloading: {p.title}')

for video in p.videos:
    (video.streams
    .filter(progressive=True, file_extension='mp4')
    .desc()
    .order_by('resolution')
    .first()
    .download()
    )
    print(video.title)