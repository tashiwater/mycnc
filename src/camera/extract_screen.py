#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import cv2


class ExtractScreen:
    def __init__(self, x1, x2, y1, y2):  # corners(x, x+w, y, y+h)
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__screen_width_mm = 110
        self.__screen_height_mm = 60

    def set_img(self, img):
        self.__img = img

    def get_screen(self):
        return self.__img[self.__y1 : self.__y2, self.__x1 : self.__x2]

    def paint_rectangle(self):
        self.rectangle_img = self.__img.copy()
        red = (0, 0, 255)
        cv2.rectangle(
            self.rectangle_img,
            (self.__x1, self.__y1),
            (self.__x2, self.__y2),
            red,
            thickness=10,
        )

    def get_img_with_rectangle(self):
        return self.rectangle_img

    def px2mm_in_screen(self, x_px, y_px):
        y_mm = x_px / self.width_px * self.__screen_width_mm
        x_mm = y_px / self.height_px * self.__screen_height_mm
        return x_mm, y_mm

    def px2mm_from_all_img(self, x_px, y_px):
        # マイコン側とx,yが逆転しているため、出力も逆転させている
        y_mm = (x_px - self.__x1) / self.width_px * self.__screen_width_mm
        x_mm = (y_px - self.__y1) / self.height_px * self.__screen_height_mm
        return x_mm, y_mm

    @property
    def width_px(self):
        return self.__x2 - self.__x1

    @property
    def height_px(self):
        return self.__y2 - self.__y1
