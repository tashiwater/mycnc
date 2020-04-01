#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=int(input("loop count:")))
        self._count = 1
    def make_data_override(self):
        
        #ストーリーが表示されたとき用
        self._datamaker.xy_abs_move(35, 2)
        self._datamaker.one_click()
        self._datamaker.wait(3000)
        
        if self._count != 1:
            self.attack_prepare()
        self.attack()
        self.origin_wait_s(100)        
        self.next_in1()
        self.next_in3()
        self.origin_wait_s(6)


            
        
        
        