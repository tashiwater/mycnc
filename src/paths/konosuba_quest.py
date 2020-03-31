#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker
import time

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=3)
        
    def make_data_override(self):

        if self._count == 1:
            #挑戦準備
            self._datamaker.xy_abs_move(15, 12)
            self._datamaker.one_click()
            self._datamaker.wait(3000)

            # 挑戦する
            self._datamaker.xy_abs_move(3, 15)
            self._datamaker.one_click()
            pass
        elif self._count == self._max_loop:
            #次へ
            self._datamaker.xy_abs_move(7,50)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
            #次へ
            self._datamaker.xy_abs_move(7,45)
            self._datamaker.one_click()
        else:
            #次へ
            self._datamaker.xy_abs_move(7,50)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
            #再戦する
            self._datamaker.xy_abs_move(7,65)
            self._datamaker.one_click()
            #OK
            self._datamaker.xy_abs_move(18,40)
            self._datamaker.one_click()
            
        #画面遷移
        self._datamaker.xy_abs_move(0,0)
        self._datamaker.wait(1000)
        
        
        