#!/usr/bin/python3.4
from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class Downloadmp3():
    """Class for download webm and convert mp3 in youtube"""

    def __init__(self, url):
        self.options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),

        }
        with youtube_dl.YoutubeDL(self.options) as ydl:
            ydl.download([url])


###########################################################
#TEST PHASE

if __name__ == "__main__":
    Downloadmp3("https://www.youtube.com/watch?v=9p7ToiJ5Q9o")
