#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet


class DataMaker:
    def __init__(self):
        self.__move_sets = [MoveSet(0, 0, 0, 0)]
        self.__offset_x_mm = 0
        self.__offset_y_mm = 0

    def set_offset(self, x_mm, y_mm):
        self.__offset_x_mm = x_mm
        self.__offset_y_mm = y_mm

    def clear(self):
        self.__move_sets = []

    def restart(self):
        self.__move_sets = [MoveSet(0, 0, 0, 0)]

    def one_click(self):
        last = self.__move_sets[-1]
        new_move = MoveSet(last.x_mm, last.y_mm, 300, last.solenoid_val)
        self.__move_sets.append(new_move)
        self.push()
        self.pull()

    def push(self):
        last = self.__move_sets[-1]
        push = MoveSet(last.x_mm, last.y_mm, 300, 1)
        self.__move_sets.append(push)

    def pull(self):
        last = self.__move_sets[-1]
        pull = MoveSet(last.x_mm, last.y_mm, 300, 0)
        self.__move_sets.append(pull)

    def get_movesets(self):
        return self.__move_sets

    def wait(self, ms):
        self.__move_sets[-1].wait_ms = ms

    def xy_abs_move(self, abs_x, abs_y):
        if self.__move_sets == []:
            last = MoveSet()
        else:
            last = self.__move_sets[-1]
        target_x = abs_x + self.__offset_x_mm
        target_y = abs_y + self.__offset_y_mm
        new_move = MoveSet(target_x, target_y, 0, last.solenoid_val)
        self.__move_sets.append(new_move)

    def go_start_position(self):
        self.__move_sets.append(MoveSet(0, 0, 0, 0))
