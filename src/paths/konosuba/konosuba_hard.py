#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time


class Path(KonosubaTool):
    def init_override(self):
        self.max_loop = int(input("course count:"))
        self._wait_time = int(input("wait time[s]:")) * 1000
        self.is_attack_prepare = input("attack prepare? y/n:")

    def make_data_override(self):
        self._datamaker.clear()
        if self.is_attack_prepare == "y":
            self.attack_prepare()
        else:
            self.is_attack_prepare = "y"
        self.attack()
        self._datamaker.wait(self._wait_time)
        for i in range(2):
            self.next_in1()
            self.rebattle_in3()
            self.ok_stamina_use()
            self._datamaker.wait(self._wait_time)
            # self.origin_wait_s(self._wait_time)
        self.next_in1()
        self.next_in3()
        self._datamaker.wait(10000)
        if self.count == self.max_loop:
            self.origin_wait_s(0)
