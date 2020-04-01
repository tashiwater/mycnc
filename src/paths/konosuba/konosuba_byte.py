#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ...base.pathmaker import PathMaker
import time

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=1)

    def make_data_override(self):
        # job
        self._datamaker.xy_abs_move(34, 5)
        self._datamaker.one_click()
        self._datamaker.wait(3000)
        # 1
        self._datamaker.xy_abs_move(13, 10)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
        # ok
        self._datamaker.xy_abs_move(8, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # 2
        self._datamaker.xy_abs_move(13, 35)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
        # ok
        self._datamaker.xy_abs_move(8, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # 3
        self._datamaker.xy_abs_move(13, 60)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
        # ok
        self._datamaker.xy_abs_move(8, 60)
        self._datamaker.one_click()
        self._datamaker.wait(500)
                # back
        self._datamaker.xy_abs_move(56, 11)
        self._datamaker.one_click()

        self._datamaker.xy_abs_move(0,0)




            
        
        
        