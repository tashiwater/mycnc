#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ...base.pathmaker import PathMaker

class KonosubaTool(PathMaker):
    def __init__(self, max_loop = None):
        super().__init__(max_loop=max_loop)
    
    
    def attack_prepare(self):
        #挑戦準備
        self._datamaker.xy_abs_move(12, 12)
        self._datamaker.one_click()
        self._datamaker.wait(3000)

    def attack(self):
        # 挑戦する
        self._datamaker.xy_abs_move(3, 15)
        self._datamaker.one_click()
    
    def next_in1(self):
        #次へ
        self._datamaker.xy_abs_move(6,50)
        self._datamaker.one_click()
        self._datamaker.wait(4000)

    def next_in2(self):
        self._datamaker.xy_abs_move(7,45)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def next_in3(self):
        #次へ 
        self._datamaker.xy_abs_move(6,30)
        self._datamaker.one_click()

    def rebattle_in2(self):
        self._datamaker.xy_abs_move(6,65)
        self._datamaker.one_click()

    def rebattle_in3(self):
        # 再戦
        self._datamaker.xy_abs_move(7, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)
    
    def ok_stamina_use(self):
        # ok
        self._datamaker.xy_abs_move(19, 40)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def course4(self):
        self._datamaker.xy_abs_move(44, 35)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
    
    def course3(self):
        self._datamaker.xy_abs_move(35, 31)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
    def course2(self):
        self._datamaker.xy_abs_move(25, 25)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
    def course1(self):
        self._datamaker.xy_abs_move(15, 25)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def ticket_plus(self):
        self._datamaker.xy_abs_move(14, 32)
        self._datamaker.one_click()
        self._datamaker.wait(500)
    
    def ticket_use(self):
        self._datamaker.xy_abs_move(14, 47)
        self._datamaker.one_click()
        self._datamaker.wait(500)

            
        
        
        