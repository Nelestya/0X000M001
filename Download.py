#!/usr/bin/python3.4
#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl
import os

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

    def movefile(directory):
        """Method for move the mp3 file in Directory Download"""
        directory = os.path.dirname(directory + "/")

        ####################################################
        #If Download in not exist Create the Directory Download
        if not os.path.exists(directory):
            os.makedirs(directory)

        dirs = os.listdir()
        for file in dirs:
            ####################################################
            #if file finish by mp3 move in directory Download
            if file[(len(file)-3):] == "mp3":
                path = directory + "/" + file
                os.rename(file, path)



###########################################################
#TEST PHASE

if __name__ == "__main__":

    Downloadmp3("https://www.youtube.com/watch?v=sB8H-lyegUc")
    Downloadmp3.movefile("Test")
