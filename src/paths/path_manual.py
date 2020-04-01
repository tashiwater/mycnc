#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker
import cv2
import readchar
import os

class Path(PathMaker):
    def __init__(self):
        super().__init__(max_loop=None) #Noneなら無限周回
        self.__old_xy = [0,0]
        self.__long_stroke_mm = 5
        self.__short_stroke_mm = 1
        current_path = os.path.dirname(os.path.abspath(__file__))
        data_path = current_path + "/../../data"
        filename = input("filename: ")
        if not filename:
            print("name -> temp.txt")
            filename = "temp.txt"
        self.__file = open(data_path + "/" + filename, mode = "w")
        self.__comment = None
        
    def make_data_override(self):
        #最終位置からスタート
        self._datamaker.clear()   
        self._datamaker.xy_abs_move(self.__old_xy[0],self.__old_xy[1])
        
        #入力文字で動作を変える
        if self.__comment is None:
            self.__comment = input("comment: ")  
            print("move by [w a s d](small: fast, Large:low)")
            print("when 0, go to origin. if y, write file")
        
        char = readchar.readkey()
        if char == "0":
            self._datamaker.xy_abs_move(0,0)
            self.__old_xy = [0,0]
        elif char == "y":
            wait_ms = input("wait_ms: ")  
            print("write")
            lines = ["# " + self.__comment+ "\n",
                    "self._datamaker.xy_abs_move({0}, {1})\n".format(self.__old_xy[0],self.__old_xy[1]),
                    "self._datamaker.one_click()\n",
                    "self._datamaker.wait({0})\n".format(wait_ms)
                    ]
            self.__file.writelines(lines)
            self.__comment = None
        elif char == "c":
            self._datamaker.one_click()
        else:
            if char.isupper():
                stroke = self.__short_stroke_mm
            else:
                stroke = self.__long_stroke_mm
            add_xy_dict = {"w":[-stroke,0], "s":[stroke,0], "a": [0,-stroke], "d":[0,stroke]}
            low_char = char.lower()
            add_xy = [0,0]
            if low_char in add_xy_dict:
                add_xy = add_xy_dict[low_char]

            target = [self.__old_xy[0] + add_xy[0],  self.__old_xy[1] + add_xy[1]]
            self._datamaker.xy_abs_move(target[0], target[1])
            self.__old_xy = target
    
    def destructor(self):
        self.__file.close()