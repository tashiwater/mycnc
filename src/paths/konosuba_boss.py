#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#このすば イベントボス再戦用
from .base.pathmaker import PathMaker
import time

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=2)
        
    def make_data_override(self):
        #再戦する
        self._datamaker.xy_abs_move(7,65)
        self._datamaker.wait(1000)
        self._datamaker.one_click()
        #OK
        self._datamaker.xy_abs_move(18,40)
        self._datamaker.wait(500)
        self._datamaker.one_click()
        #原点に戻る
        self._datamaker.xy_abs_move(0,0)
        #70秒待つ
        if self._count != 1: #1週目はやらない
            time.sleep(70) #データでは送らない。(再起動まで70秒かかってしまう。)

        
        