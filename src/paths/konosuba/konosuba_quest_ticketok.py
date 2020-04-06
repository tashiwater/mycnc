#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=int(input("loop count:")))
        self.__from_attack = input("from attack? (y/n)")

    def make_data_override(self):
        if self.__from_attack == "y":
            self.attack()
            self.__from_attack = None
            self.origin_wait_s(45)
        else:
            self.next_in1()
            self.rebattle_in3()
            self.ok_stamina_use()
            self.origin_wait_s(45)
            if self._count == self._max_loop:
                self.next_in1()
                self.next_in3()
                self.origin_wait_s(0)
        
        