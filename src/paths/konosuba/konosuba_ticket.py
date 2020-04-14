#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
from ..base.pycolor import pycolor
import time


class Path(KonosubaTool):
    def __init__(self,video):
        start_num = int(input("start num:"))
        count = input(pycolor.RED + "Warn: this might use kuorts."+pycolor.END+ " loop count: ")
        super().__init__(video,max_loop=int(count))
        
        self._count = start_num -1 #途中から始めるときはここをstart-1にする

    def make_data_override(self):
        self._datamaker.clear()
        if self._count == 1:
            self.course4()
        elif self._count == 2:
            self.course3()
        elif self._count == 3:
            self.course2()
        else:
            self.course1()
        
        for _ in range(2):
            self.ticket_plus()
        
        self.ticket_use()
        # ok
        self.ok_stamina_use()
        self._datamaker.wait(6000)
        
        self._datamaker.xy_abs_move(13.0,94.0)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # back
        self.back()

        self.origin_wait_s(0)



        
