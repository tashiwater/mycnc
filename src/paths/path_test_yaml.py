#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker

class Path(PathMaker):
    def __init__(self, video):
        super().__init__(None, max_loop=1) #Noneなら無限周回
        self.set_db("test.yaml")
        
    def make_data_override(self):
        #具体的な処理を入れる
        self.from_db("test")
        self.from_db("test2")
        self.origin_wait_s(2)
        #事あるごsとに原点に戻りましょう。リセットがしやすくなります
        # self.origin_wait_s(70)
        