#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker

class PathShimizuReverse(PathMaker):
    def __init__(self):
        super().__init__(max_loop=2)
        
    def make_data_override(self):
        #初期化
        self.data_reset()
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
        self._datamaker.wait(70000)
        