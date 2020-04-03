#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=1)

    def make_data_override(self):
        self._datamaker.xy_abs_move(25.0,100.0)
        self._datamaker.one_click()
        self._datamaker.wait(4000)
        # 1
        self._datamaker.xy_abs_move(47, 90)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
                # ok
        self._datamaker.xy_abs_move(52, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # 2
        self._datamaker.xy_abs_move(47, 70)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
        # ok
        self._datamaker.xy_abs_move(52, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # 3
        self._datamaker.xy_abs_move(47, 45)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
        # ok
        self._datamaker.xy_abs_move(52, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)

                # back
        self.back()
        self.origin_wait_s(0)



            
        
        
        