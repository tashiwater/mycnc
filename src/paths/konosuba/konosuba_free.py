#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=3)
        self._count = 2

    def make_data_override(self):
        
        if self._count == 2:
            # experience
            self._datamaker.xy_abs_move(39, 35)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
        elif self._count == 3:
            # madgic
            self._datamaker.xy_abs_move(39, 20)
            self._datamaker.one_click()
            self._datamaker.wait(2000)

        if self._count != 1:  
            self.course4()
            self.attack_prepare()     

        self.attack()        
        self.origin_wait_s(80)
        self.next_in1()
        self.rebattle_in3()
        self.ok_stamina_use()
        self.origin_wait_s(80)
        self.next_in1()
        self.next_in3()
        self.origin_wait_s(10)
        