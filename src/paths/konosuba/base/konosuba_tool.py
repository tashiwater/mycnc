#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ...base.pathmaker import PathMaker


class KonosubaTool(PathMaker):
    def init_override(self):
        self._datamaker.set_offset(1, 0)

    def attack_prepare(self):
        # 挑戦準備
        self._datamaker.xy_abs_move(45, 93)
        self._datamaker.one_click()
        self._datamaker.wait(3000)

    def attack(self):
        # 挑戦する
        self._datamaker.xy_abs_move(55, 90)
        self._datamaker.one_click()

    def next_in1(self):
        # 次へ
        self.rebattle_in3()
        self._datamaker.wait(4000)

    def next_in2(self):
        self._datamaker.xy_abs_move(55, 60)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def next_in3(self):
        # 次へ
        self._datamaker.xy_abs_move(54.0, 75.0)
        self._datamaker.one_click()

    def rebattle_in2(self):
        self._datamaker.xy_abs_move(56.0, 40.0)
        self._datamaker.one_click()

    def rebattle_in3(self):
        # 再戦
        self._datamaker.xy_abs_move(55.0, 50.0)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def ok_stamina_use(self):
        # ok
        self._datamaker.wait(1000)
        self._datamaker.xy_abs_move(40.0, 65.0)
        self._datamaker.one_click()
        self._datamaker.wait(500)
        # self._datamaker.xy_abs_move(42.0, 63.0)
        # self._datamaker.one_click()
        # self._datamaker.wait(500)

    def wait_konosuba(self, s):
        self._datamaker.xy_abs_move(20, 65.0)
        self._datamaker.wait(s * 1000)


    def course4(self):
        self._datamaker.xy_abs_move(18.0, 70.0)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def course3(self):
        self._datamaker.xy_abs_move(25.0, 74.0)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def course2(self):
        self._datamaker.xy_abs_move(34.0, 80.0)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def course1(self):
        self._datamaker.xy_abs_move(42.0, 80.0)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def ticket_plus(self):
        self._datamaker.xy_abs_move(47.0, 73.0)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def ticket_use(self):
        self._datamaker.xy_abs_move(47.0, 58.0)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def back(self):
        self._datamaker.xy_abs_move(3.0, 94.0)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def ok1(self):
        self._datamaker.xy_abs_move(52, 55)
        self._datamaker.one_click()
        self._datamaker.wait(500)

    def home(self):
        self._datamaker.xy_abs_move(60, 15)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def quest(self):
        self._datamaker.xy_abs_move(57, 29)
        self._datamaker.one_click()
        self._datamaker.wait(3000)

    def event(self):
        # 使えない
        self._datamaker.xy_abs_move(45, 95)
        self._datamaker.one_click()
        self._datamaker.wait(3000)

    def free_quest(self):
        self._datamaker.xy_abs_move(40, 65)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def event_quest(self):
        self._datamaker.xy_abs_move(20, 70)
        self._datamaker.one_click()
        self._datamaker.wait(2000)

    def quest_hard(self):
        self._datamaker.xy_abs_move(5, 80)
        self._datamaker.one_click()
        self._datamaker.wait(2000)
