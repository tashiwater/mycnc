#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=None) #Noneなら無限周回
        self.count = 0
        
    def make_data_override(self):
        #具体的な処理を入れる
        self._datamaker.push()
        #事あるごとに原点に戻りましょう。リセットがしやすくなります
        # self.origin_wait_s(70)
        