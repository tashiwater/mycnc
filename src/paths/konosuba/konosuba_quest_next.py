#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from .base.konosuba_tool import KonosubaTool


class Path(KonosubaTool):
    def __init__(self,video):
        super().__init__(video,max_loop=int(input("loop count:")))
        # self._count = 0
        self.__from_prepare = input("from attack prepare (y/n):")
    def make_data_override(self):
        
        #ストーリーが表示されたとき用
        self._datamaker.xy_abs_move(16.0,94.0)
        self._datamaker.one_click()
        self._datamaker.wait(3000)
        
        if self.__from_prepare == "y":
            self.attack_prepare()
        else:
            self.__from_prepare = "y" #2回目以降は挑戦準備からやる
        self.attack()
        self.origin_wait_s(100)        
        self.next_in1()
        self.next_in3()
        self.origin_wait_s(12)


            
        
        
        