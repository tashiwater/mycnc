#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# このすば アリーナ用
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=3)
        self._count = 0
        
    def make_data_override(self):
        if self._count != 1: 
            #コース選択
            self._datamaker.xy_abs_move(30, 15)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
            #挑戦準備
            self.attack_prepare()
            #初回だけここまで手動
            
        # 挑戦する
        self.attack()
        self.origin_wait_s(95)
        self.next_in1()
        self.next_in1()
        
        #ゲット Ok
        self._datamaker.xy_abs_move(8, 50)
        self._datamaker.one_click()
        self._datamaker.wait(1000)
        self.next_in1()
        self.origin_wait_s(6)

        
        