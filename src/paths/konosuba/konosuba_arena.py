#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# このすば アリーナ用
from .base.konosuba_tool import KonosubaTool


class Path(KonosubaTool):
    def __init__(self, video=None):
        super().__init__(video, max_loop=3)
        self._count = 0

    def make_data_override(self):
        if self._count != 1:
            # コース選択
            self._datamaker.xy_abs_move(29.0, 90.0)
            self._datamaker.one_click()
            self._datamaker.wait(2000)
            # アリーナに挑戦する
            self._datamaker.xy_abs_move(47.0, 70.0)
            self._datamaker.one_click()
            self._datamaker.wait(3000)
            # 初回だけここまで手動

        # 挑戦する
        self.attack()
        self.origin_wait_s(105)
        self.next_in1()
        self.next_in1()

        # ゲット Ok
        self.ok1()
        self.next_in1()
        if self._count == self._max_loop:
            self.back()  # [TODO]なぜかソレノイドが動かない。動こうとする音はする. loop=1だと動く
            self.back()
        self.origin_wait_s(6)
