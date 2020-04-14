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

    def go_hard(self):
        # self.quest()
        # self.event()
        self.event_quest()
        self.quest_hard()

    def make_data_override(self):
        self._datamaker.clear()
        if self._count == 1:
            self.go_hard()

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
        self._datamaker.xy_abs_move(40.0,64.0)
        self._datamaker.one_click()
        self._datamaker.wait(5000)
        # ok
        self.ok1()
        # self._datamaker.xy_abs_move(51.0,49.0)
        # self._datamaker.one_click()
        # self._datamaker.wait(500)
        # back
        self.back()

        if self._count == self._max_loop:
            self.back()
            self.origin_wait_s(0)



        
