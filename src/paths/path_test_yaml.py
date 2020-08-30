#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker


class Path(PathMaker):
    def init_override(self):
        self.max_loop = 1
        self.set_db("temp.yaml")

    def make_data_override(self):
        # 具体的な処理を入れる
        self.from_db("a")
        # self.from_db("test2")
        self.origin_wait_s(2)
        # 事あるごsとに原点に戻りましょう。リセットがしやすくなります
        # self.origin_wait_s(70)
