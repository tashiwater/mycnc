#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker
import math
class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=1) #Noneなら無限周回
        
    def make_data_override(self):
        #具体的な処理を入れる
        # self._datamaker.push()

        r = 20
        num = 50
        rads = [math.pi * 2 *i/num  for i in range(num)]
        for i ,rad in enumerate(rads):
            x = r * math.cos(rad) + r + 5
            y = r * math.sin(rad) + r + 5
            self._datamaker.xy_abs_move(x,y)
            # if i == 0:
            #     self._datamaker.push()
            self._datamaker.one_click()
            # self._datamaker.wait(100)
        # self._datamaker.push()
        #事あるごとに原点に戻りましょう。リセットがしやすくなります
        self.origin_wait_s(0)
        