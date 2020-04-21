from mutagen.mp3 import MP3 as mp3
import pygame
import time
import os

class Mp3Player:
    def __init__(self, sounds_folder):
        self.sounds_folder = sounds_folder
        pygame.mixer.init()

    def play_mp3(self, file_name):
        target_path = self.sounds_folder + file_name
        pygame.mixer.music.load(target_path) #音源を読み込み
        mp3_length = mp3(target_path).info.length #音源の長さ取得
        pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
        time.sleep(mp3_length + 0.8) #再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
        pygame.mixer.music.stop() #音源の長さ待ったら再生停止

class Speaker(Mp3Player):
    def __init__(self, sounds_folder):
        self.__player = Mp3Player(sounds_folder)
        
    def output_bye(self):
        otukare =  'line-girl1-otsukaresamadeshita1.mp3' #再生したいmp3ファイル
        self.__player.play_mp3(otukare)
        sorezya =  "line-girl1-sorezyane1.mp3"
        self.__player.play_mp3(sorezya)
        bye = "line-girl1-byebye1.mp3"
        self.__player.play_mp3(bye)

    def play(self,file_name):
        self.__player.play_mp3(file_name)


