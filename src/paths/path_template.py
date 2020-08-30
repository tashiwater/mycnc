#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker


class Path(PathMaker):
    def init_override(self):
        # 以下は好きにいじる
        self.max_loop = 1  # Noneなら無限周回
        self.set_db("test.yaml")  # yamlファイル読み込み

    def make_data_override(self):
        # 具体的な処理を入れる

        # 例: yamlを使う
        self.from_db("test")
        self.from_db("test2")

        # 例: 直接打ち込む
        self._datamaker.xy_abs_move(10, 10)
        self._datamaker.one_click()
        self._datamaker.pull()
        self._datamaker.push()
        self._datamaker.wait(500)

        # 事あるごとに原点に戻りましょう。リセットがしやすくなります
        self.origin_wait_s(1)
