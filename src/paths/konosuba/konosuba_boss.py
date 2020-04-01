#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#このすば イベントボス再戦用
from .base.konosuba_tool import KonosubaTool
import time

class Path(KonosubaTool):
    def __init__(self):
        super().__init__(max_loop=int(input("loop count:")))
        
    def make_data_override(self):
        self.rebattle_in2()
        self.ok_stamina_use()
        self.origin_wait_s(100)

        
        