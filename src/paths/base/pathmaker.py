#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
from .datamaker import DataMaker
class PathMaker:
    def __init__(self, max_loop = None): #max_loop:Noneなら無限周回
        self._datamaker = DataMaker()
        self._count = 0
        self.__max_loop = max_loop
    
    def data_reset(self):
        self._datamaker = DataMaker()

    def get_datas(self):
        return self._datamaker.get_movesets()

    def make_data_override(self):
        #ここを継承先で実行してもらう
        pass

    def make_data_loop(self):
        if self.__max_loop is not None:
            self._count+=1
            if (self._count > self.__max_loop):
                self._datamaker.no_data()
                return
        self.make_data_override()


    def get_wait_sum(self):
        wait = 0
        for data in self.get_datas():
            wait += data.wait_ms
        return wait
    
    def show_datas(self):
        for data in self.get_datas():
            print(data.get_data_str())
        