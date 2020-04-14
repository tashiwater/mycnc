#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
from .datamaker import DataMaker


import os

class PathMaker:
    def __init__(self, video = None, max_loop = None, ): #max_loop:Noneなら無限周回
        self._datamaker = DataMaker()
        self._count = 0
        self._max_loop = max_loop
        self._video = video

    def video_start(self):
        if self._video is not None:
            print("d")
            self._video.start()

    def video_save(self):
        if self._video is not None:
            self._video.stop()
            
            #現在時刻でmp4ファイル生成
            current_path = os.path.dirname(os.path.abspath(__file__))
            self.movie_folder = current_path + "./../../../data/movie/"
            import datetime
            now = datetime.datetime.now()
            filename = self.movie_folder + now.strftime('%Y%m%d_%H%M%S') + '.mp4'
            self._video.save(filename)

    def __del__(self):
        self.video_save()
    
    @property
    def count(self):
        return self._count

    def get_datas(self):
        return self._datamaker.get_movesets()

    def make_data_override(self):
        #ここを継承先で実行してもらう
        pass
    
    def make_data_loop(self):
        if self._max_loop is not None:
            self._count+=1
            if (self._count > self._max_loop):
                self._datamaker.clear()
                return
        #初期化
        self._datamaker.restart()
        #経路作成 継承先クラスで実装
        self.make_data_override()

        #一番最後の指示するwaitは0。(あるとマイコンが動作終了後もwaitしてしまう)
        #代わりにpythonをsleepする
        self.__last_wait_ms = self.get_datas()[-1].wait_ms
        self._datamaker.wait(0)


    def get_wait_sum(self):
        wait = 0
        for data in self.get_datas():
            wait += data.wait_ms
        return wait + self.__last_wait_ms
    
    def show_datas(self):
        for data in self.get_datas():
            print(data.get_data_str())
    
    def origin_wait_s(self, s):
        #原点で待つ
        self._datamaker.go_start_position()
        self._datamaker.wait(s * 1000)
        