#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker

class PathShimizu(PathMaker):
    def make_data(self):
        #初期化
        self.data_reset()


        # """
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
        
        # """