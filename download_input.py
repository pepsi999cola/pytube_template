from pytube import YouTube

url = input('URLを入力してください:')
yt = YouTube(url)  # 動画のurlを入力

#字幕
# caption = yt.captions.get_by_language_code('a.ja')
# print(caption.xml_captions)

(yt.streams
    .get_highest_resolution()
    .download()
)

# caption = yt.captions.get_by_language_code('en')
# caption = caption.xml_captions
print(yt.title)
print(url)
