#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# このすば アリーナ用
from .base.pathmaker import PathMaker
import time

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=1)
        
    def make_data_override(self):
        if self._count != 1: 
            #コース選択
            self._datamaker.xy_abs_move(30, 15)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
            #挑戦準備
            self._datamaker.xy_abs_move(12, 30)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
            #初回だけここまで手動
            
        # 挑戦する
        self._datamaker.xy_abs_move(3, 15)
        self._datamaker.one_click()

        #画面遷移
        self._datamaker.wait(88000)
        
        self._datamaker.xy_abs_move(5, 50)
        self._datamaker.one_click()
        self._datamaker.wait(1000)
        #次へ
        self._datamaker.xy_abs_move(5, 50)
        self._datamaker.one_click()
        #ゲット Ok
        self._datamaker.xy_abs_move(8, 50)
        self._datamaker.one_click()
        self._datamaker.wait(1000)
        #次へ
        self._datamaker.xy_abs_move(6, 50)
        self._datamaker.one_click()
        #原点に戻る
        self._datamaker.xy_abs_move(0,0)
        self._datamaker.wait(6000)

        
        