from pytube import YouTube
from pytube import Playlist
import os
import subprocess
import time

class YTdl:
    mp3_ext = '.mp3'
    mp4_ext = '.mp4'

    def __init__(self, video=False, mp3=True, dest='C:/Users/may/Downloads/ytdl/', wait=3):
        self.dest_dir = dest
        if not os.path.exists(self.dest_dir):
            os.makedirs(self.dest_dir)
        os.chdir(self.dest_dir)
        self.video = video
        self.mp3 = mp3
        self.wait = wait

    def download(self, url):
        try:
            yt = YouTube(url)
        except TimeoutError as e:
            print(url + 'skipped')
            print(e)
            pass
        name = yt.title
        mp3_name = name + self.mp3_ext
        mp4_name = name + self.mp4_ext

        for p, d, f in os.walk(self.dest_dir):
            for file in f:
                if (self.mp3 and file == mp3_name) or (not self.mp3 and file.startswith(name)):
                    print(name + ' already exists, skip.')
                    return

        if self.mp3 or not self.video:
            s = yt.streams.get_audio_only()

        else:
            s = yt.streams.first()
        print('Downloading '+ name + ' ......')
        s.download(self.dest_dir)
        time.sleep(self.wait)

        if self.mp3:
            mp3_name = '\"' + mp3_name + '\"'
            mp4_name = '\"' + mp4_name + '\"'
            convert = ('ffmpeg -i ' + mp4_name + ' ' + mp3_name +' && del /f ' + mp4_name)

            print(convert)
            subprocess.call(convert, shell=True)
            print('complete')

    def download_playlist(self, url):
        p = Playlist(url)
        urls = p.video_urls
        total = str(len(urls))
        i = 1
        for u in urls:
            print(str(i) + '/' + total)
            self.download(u)
            i += 1