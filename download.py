from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=') #動画のurlを入力
yt.streams.filter(progressive=True, file_extension='mp4').desc().order_by('resolution').first().download()
# caption = yt.captions.get_by_language_code('en')
# caption = caption.xml_captions
print(yt.title)
