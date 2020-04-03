#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
#  エリスクエストに[挑戦する] で呼び出す
class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=3)
        self._count = 1


    def make_data_override(self):
        if self._count == 1:
            self.quest()
            self.free_quest()

        course_dict = {1:[19.0,50.0], 2:[20.0,70.0], 3:[20.0,85.0]} #エリス、経験値、魔法の順
        target_xy = course_dict[self._count]
        self._datamaker.xy_abs_move(target_xy[0], target_xy[1])
        self._datamaker.one_click()
        self._datamaker.wait(2000)

        self.course4()
        for _ in range(1):
            self.ticket_plus()
        
        self.ticket_use()
        # ok
        self._datamaker.xy_abs_move(40.0,64.0)
        self._datamaker.one_click()
        self._datamaker.wait(5000)
        # ok
        self.ok1()

        if self._count == self._max_loop:
            self.back()
    
        self._datamaker.xy_abs_move(0,0)
        