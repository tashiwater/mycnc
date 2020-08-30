#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import cv2

CAMERA_PORT = 2

class Camera():
    def __init__(self):
        self.__screen_width_mm = 110
        self.__screen_height_mm = 60

    def setScreenSizeMM(self, width_mm, height_mm):
        self.__screen_width_mm = width_mm
        self.__screen_height_mm = height_mm

    def setContoursParam(self,  min_w, min_h, thresh = 125, max_w=500, max_h=2000):
        self.__contours = Contours(thresh, min_w, min_h, max_w, max_h)
    
    # 短形抽出開始, 領域を返す
    def findContours(self):
        im = cv2.VideoCapture(CAMERA_PORT)
        ret, frame = im.read()
        # cv2.imshow("test", frame)
        # cv2.waitKey(0)
        self.__contours.setImage(frame)
        return self.__contours.find_contours()

    # 抽出された領域をもとに画像を切り取って返す
    def capture(self):
        im = cv2.VideoCapture(CAMERA_PORT)
        ret, frame = im.read()
        for roi_img in self.__contours.get_rectangle_img():
            return roi_img

if __name__ == '__main__':
    camera = Camera()
    camera.setContoursParam(min_w = 100, min_h = 100)
    ret = camera.findContours()
    cv2.imshow("frame2", ret)
    cv2.imshow("frame", camera.capture())
    cv2.waitKey(0)


