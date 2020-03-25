#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
from .datamake_tool import DataMaker
class PathMaker:
    def __init__(self):
        self._datamaker = DataMaker()
    
    def get_datas(self):
        return self._datamaker.get_movesets()

    def make_data(self):
        #初期化
        self._datamaker = DataMaker()
        self._datamaker.push()
        self._datamaker.xy_abs_move(50,0)
        self._datamaker.pull()
        self._datamaker.xy_abs_move(0,0)

        """
        val = 40
        for i in range(4):
            self._datamaker.xy_abs_move(0,val)
            self._datamaker.wait(500)
            self._datamaker.xy_abs_move(val,val)
            self._datamaker.wait(500)
            self._datamaker.xy_abs_move(val,0)
            self._datamaker.wait(500)
            self._datamaker.xy_abs_move(0,0)
            self._datamaker.wait(500)
            # self._datamaker.xy_abs_move(0,0)
"""

        """
        #編成へ
        self._datamaker.xy_abs_move(50,85)
        self._datamaker.wait(1000)
        self._datamaker.one_click()
        #出撃
        self._datamaker.xy_abs_move(55,90)
        self._datamaker.wait(1000)
        self._datamaker.one_click()


        self._datamaker.xy_abs_move(52,53)
        self._datamaker.wait(1000)
        self._datamaker.one_click()
        self._datamaker.xy_abs_move(52,53)
        self._datamaker.wait(1000)
        self._datamaker.one_click()
        self._datamaker.xy_abs_move(40,65)
        self._datamaker.wait(1000)
        self._datamaker.one_click()
        self._datamaker.xy_abs_move(0,0)
        """

    def get_wait_sum(self):
        wait = 0
        for data in self.get_datas():
            wait += data.wait_ms
        return wait
    
    def show_datas(self):
        for data in self.get_datas():
            print(data.get_data_str())
        