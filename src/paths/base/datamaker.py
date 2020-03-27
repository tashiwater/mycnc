#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
import copy
class DataMaker:
    def __init__(self):
        self.__move_sets = [MoveSet(0,0,0,0)]

    def set_movesets(self, move_sets):
        self.__move_sets = copy.deepcopy(move_sets)

    def xy_move(self, add_x, add_y):
        last = self.__move_sets[-1]
        new_move = MoveSet(last.x_mm + add_x, last.y_mm + add_y, 0, last.solenoid_val)
        self.__move_sets.append(new_move)
    
    def one_click(self):
        self.push()
        self.pull()
    
    def push(self):
        last = self.__move_sets[-1]
        push = MoveSet(last.x_mm, last.y_mm, 300, 1)
        self.__move_sets.append(push)

    def pull(self):
        last = self.__move_sets[-1]
        pull = MoveSet(last.x_mm, last.y_mm, 500, 0)
        self.__move_sets.append(pull)
    
    def get_movesets(self):
        return self.__move_sets
    
    def wait(self, ms):
        self.__move_sets[-1].wait_ms = ms
    
    def xy_abs_move(self, abs_x, abs_y):
        last = self.__move_sets[-1]
        new_move = MoveSet(abs_x, abs_y, 0, last.solenoid_val)
        self.__move_sets.append(new_move)


    