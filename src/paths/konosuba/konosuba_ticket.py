#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
from ..base.pycolor import pycolor
import time


class Path(KonosubaTool):
    def __init__(self):
        count = input(pycolor.RED + "Warn: this might use kuorts."+pycolor.END+ " loop count: ")
        super().__init__(max_loop=int(count))
        self._count = 0 #途中から始めるときはここをstart-1にする

    def make_data_override(self):
        
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
        self._datamaker.xy_abs_move(19, 41)
        self._datamaker.one_click()
        self._datamaker.wait(5000)
        # ok
        self._datamaker.xy_abs_move(8, 56)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # back
        self._datamaker.xy_abs_move(56, 11)
        self._datamaker.one_click()

        self._datamaker.xy_abs_move(0,0)
        self._datamaker.wait(2000)

        
