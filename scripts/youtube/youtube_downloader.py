from pytube import YouTube
import os

print('mulai dong aah...')
# list all the log
basepath = "notepad/"
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        with open(os.path.join(basepath, entry), "r", encoding="utf-8") as f:
            content = f.readlines()

        for item in content:
            YouTube(item).streams.first().download('/video')
            # yt = YouTube(item)
            # yt = yt.get('mp4', '720p')
            # yt.download('/video')

print('kelar.....')
