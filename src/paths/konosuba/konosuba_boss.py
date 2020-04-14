#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#このすば イベントボス再戦用
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self,video):
        super().__init__(video, max_loop=int(input("loop count:")))
        self.__from_attack = input("from atack? y/n:")
        
    def make_data_override(self):
        if self.__from_attack == "y":
            self.__from_attack = "n"
            self.attack() 
        else:
            self.rebattle_in2()
            self.ok_stamina_use()
        self.origin_wait_s(70)  # 最高難度:100 一つ下：70

        if self._count == self._max_loop:
            self.next_in2()
            self.origin_wait_s(0)

             


        
        