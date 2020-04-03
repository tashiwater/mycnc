#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
import copy
import os

class DataMaker:
    def __init__(self):
        self.__move_sets = [MoveSet(0,0,0,0)]
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.__log_folder = current_path + "./../../../data/log/"
        self.__is_reverse = False
        self.__offset_x_mm = 0
        self.__offset_y_mm = 0
    def set_reverse(self, is_reverse):
        self.__is_reverse = is_reverse
    
    def get_reverse(self):
        return self.__is_reverse
    def set_offset(self, x_mm, y_mm):
        self.__offset_x_mm = x_mm
        self.__offset_y_mm = y_mm
    def set_center(self,center_x_mm, center_y_mm): #画面反転の回転中心
        self.__center_x_mm = center_x_mm
        self.__center_y_mm = center_y_mm
    
    def clear(self):
        self.__move_sets = []
    
    def restart(self):
        self.__move_sets = [MoveSet(0,0,0,0)]
        
    def one_click(self):
        last = self.__move_sets[-1]
        new_move = MoveSet(last.x_mm, last.y_mm , 300, last.solenoid_val)
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
        if self.__is_reverse is True:
            moved_x = abs_x - self.__center_x_mm
            moved_y = abs_y - self.__center_y_mm 
            moved_x *= -1
            moved_y *= -1
            target_x = moved_x + self.__center_x_mm
            target_y = moved_y + self.__center_y_mm
        else:
            target_x, target_y = abs_x, abs_y
        
        new_move = MoveSet(target_x + self.__offset_x_mm, target_y + self.__offset_y_mm, 0, last.solenoid_val)
        self.__move_sets.append(new_move)
    
    #[TODO] manager側に任せるべき
    def write_csv(self, file_name):
        file_path = self.__log_folder + file_name
        with open(file_path) as f:
            f.write(MoveSet.get_title() + "\n")
            for data in self.__move_sets:
                f.write(data.get_data_str() + "\n")
    
    def go_start_position(self):
        self.__move_sets.append(MoveSet(0, 0, 0, 0))

    



    