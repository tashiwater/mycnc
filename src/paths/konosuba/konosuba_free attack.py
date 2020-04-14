#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time
#  エリスクエストに[挑戦する] で呼び出す
class Path(KonosubaTool):
    def __init__(self,video):
        super().__init__(video,max_loop=3)

    def make_data_override(self):
        if self._count != 1:
            course_dict = {1:[19.0,50.0], 2:[20.0,70.0], 3:[20.0,85.0]} #エリス、経験値、魔法の順
            target_xy = course_dict[self._count]
            self._datamaker.xy_abs_move(target_xy[0], target_xy[1])
            self._datamaker.one_click()
            self._datamaker.wait(2000)
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
        