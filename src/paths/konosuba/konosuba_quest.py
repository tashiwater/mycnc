#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=1)
        
    def make_data_override(self):
        #次へ
        self.next_in1()
        if self._count == self._max_loop:
            # self._datamaker.xy_abs_move(7,50)
            # self._datamaker.one_click()
            # self._datamaker.wait(2000)
            #次へ
            self.next_in2()
        else:
            self.rebattle_in2()
            self.ok_stamina_use()
            
        #画面遷移
        self.origin_wait_s(150)
        
        
        