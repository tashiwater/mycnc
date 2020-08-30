#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self,video = None):
        super().__init__(video,max_loop=int(input("loop count:")))
        self.__from_attack = input("from attack? (y/n)")

    def make_data_override(self):
        if self.__from_attack == "y":
            self.attack()
            self.__from_attack = None
        else:
            self.next_in1()
            self.rebattle_in2()
            self.ok_stamina_use()
            self.origin_wait_s(150)
            if self._count == self._max_loop:
                self.next_in2()
                self.origin_wait_s(0)
        
        