#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .base.pathmaker import PathMaker
from .base.extract_screen import ExtractScreen
import cv2
class Path(PathMaker):
    def __init__(self, video):
        super().__init__(video, max_loop=None) #Noneなら無限周回
        self.__extract_screen = ExtractScreen((62, 1148, 166, 720))
    
    def make_data_override(self):
        #具体的な処理を入れる

        # self._datamaker.xy_abs_move(10,10)
        # self._datamaker.one_click()
        # self._datamaker.pull()
        # self._datamaker.push()
        # self._datamaker.wait(500)
        frame = self._video.get_frame()
        self.__extract_screen.set_img(frame)
        screen_img = self.__extract_screen.get_screen()
        cv2.imshow("frame", frame)
        cv2.imshow("screen", screen_img)
        cv2.waitKey(1)
        #事あるごとに原点に戻りましょう。リセットがしやすくなります
        self.origin_wait_s(0)
        ret = input("q->exit")
        if ret == "q":
            self._datamaker.restart()
        cv2.destroyAllWindows()

    
    def __del__(self):
        super().__del__()
        cv2.destroyAllWindows()