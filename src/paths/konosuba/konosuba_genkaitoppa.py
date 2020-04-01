#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ..base.pathmaker import PathMaker
import time

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=int(input("loop count:")))

    def make_data_override(self):
        # 限界突破
        self._datamaker.xy_abs_move(18, 32)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # ok
        self._datamaker.xy_abs_move(8, 42)
        self._datamaker.one_click()
        self._datamaker.wait(5000)
        # 画面遷移
        self._datamaker.one_click()

        self._datamaker.xy_abs_move(0, 0)
        self._datamaker.wait(1000)

        



            
        
        
        