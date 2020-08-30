#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time


class Path(KonosubaTool):
    def __init__(self, video=None):
        super().__init__(video, max_loop=int(input("loop count:")))
        self.__from_attack = input("from attack? (y/n):")
        self._wait_s = 40

    def make_data_override(self):
        self._datamaker.clear()
        if self.__from_attack == "y":
            self.attack()
            self.__from_attack = None
            self._datamaker.wait(40000)
        else:
            self.next_in1()
            self.rebattle_in3()
            self.ok_stamina_use()
            # self._datamaker.xy_abs_move(55.0, 50.0)
        # 戦闘中
            self.wait_konosuba(40)
        if self._count == self._max_loop:
            self.next_in1()
            self.next_in3()
            self.origin_wait_s(0)
