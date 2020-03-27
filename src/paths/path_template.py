#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker

class PathName(PathMaker):
    def __init__(self):
        super().__init__(max_loop=None) #Noneなら無限周回
        
    def make_data_override(self):
        #初期化
        self.data_reset()
        
        #具体的な処理を入れる


        #原点に戻る
        self._datamaker.xy_abs_move(0,0)
        self._datamaker.wait(70000)
        