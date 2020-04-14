#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self,video):
        super().__init__(video,max_loop=int(input("loop count:")))
        self.__from_attack = input("from attack? (y/n)")
        self._datamaker.set_offset(3,0)

    def make_data_override(self):
        if self.__from_attack == "y":
            self.attack()
            self.__from_attack = None
        else:
                    #ストーリーが表示されたとき用
            self._datamaker.xy_abs_move(16.0,94.0)
            self._datamaker.one_click()
            self.next_in1()
            self.rebattle_in3()
            self.ok_stamina_use()
        #戦闘中
        self.origin_wait_s(65)
        if self._count == self._max_loop:
            self.next_in1()
            self.next_in3()
            self.origin_wait_s(0)
        
        