#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker

class Path(PathMaker):
    def __init__(self, video):
        super().__init__(video, max_loop=2) #Noneなら無限周回
        
    def make_data_override(self):
        #具体的な処理を入れる

        # self._datamaker.xy_abs_move(10,10)
        # self._datamaker.one_click()
        # self._datamaker.pull()
        # self._datamaker.push()
        # self._datamaker.wait(500)


        #事あるごsとに原点に戻りましょう。リセットがしやすくなります
        self.origin_wait_s(0)
        input("input")