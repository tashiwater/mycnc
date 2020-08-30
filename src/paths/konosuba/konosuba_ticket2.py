#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.konosuba_tool import KonosubaTool


class Path(KonosubaTool):
    def init_override(self):
        self._datamaker.set_offset(1, 0)
        self.max_loop = int(input("loop count:"))
        self.set_db("konosuba.yaml")

    def make_data_override(self):
        self._datamaker.clear()
        for _ in range(2):
            self.ticket_plus()
        self.ticket_use()
        # ok
        self.ok_stamina_use()
        self._datamaker.wait(6000)

        self._datamaker.xy_abs_move(15.0, 94.0)
        self._datamaker.one_click()
        self._datamaker.wait(500)

        if self.count != self.max_loop:
            self.from_db("quest_slide")
        else:
            self.back()
            self.origin_wait_s(0)

        # back
