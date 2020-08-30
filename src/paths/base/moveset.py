#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class MoveSet:
    def __init__(self, x_mm = 0, y_mm = 0, wait_ms=0, solenoid_val=0):
        self.x_mm = int(x_mm)
        self.y_mm = int(y_mm)
        self.wait_ms = int(wait_ms)
        self.solenoid_val = int(solenoid_val)
    
    @classmethod
    def get_title(self):
        return "x_mm,y_mm,wait_ms,solenoid_val"

    def get_data_str(self):
        return str(self.x_mm) + "," + str(self.y_mm) + "," + str(self.wait_ms) + "," + str(self.solenoid_val)