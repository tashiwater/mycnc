#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
from .datamaker import DataMaker
class PathMaker:
    def __init__(self):
        self._datamaker = DataMaker()
    
    def data_reset(self):
        self._datamaker = DataMaker()

    def get_datas(self):
        return self._datamaker.get_movesets()

    def make_data(self):
        pass

    def get_wait_sum(self):
        wait = 0
        for data in self.get_datas():
            wait += data.wait_ms
        return wait
    
    def show_datas(self):
        for data in self.get_datas():
            print(data.get_data_str())
        