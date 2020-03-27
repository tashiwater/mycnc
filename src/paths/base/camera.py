#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import cv2

CAMERA_PORT = 1

class Contours():
    def __init__(self, thresh, min_w, min_h, max_w=1000, max_h=1000):
        self.thresh = thresh
        self.__min_w = min_w
        self.__min_h = min_h
        self.__max_w = max_w
        self.__max_h = max_h

    def setImage(self, img):
        self.raw_img = img.copy()
        self.img = img.copy()
    
    def find_contours(self):
        img = self.img
        # 二値化
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 画像を平滑化(白色雑音の除去). ksize:フィルタ窓枠の大きさ, sigmaX: ガウシアンの標準偏差値. 0だとカーネルのサイズから自動的に計算
        graygauss = cv2.GaussianBlur(gray, ksize=(3, 3), sigmaX=0)
        # 二値化. thresh:閾値.  maxval:閾値以上(指定により閾値以下のこともある)の値を持つ画素に対して割り当てられる値,
        # type:二値化の方法。cv2.THRESH_BINARY_INVだと白黒かつ反転
        # 返り値:[1]に画像が入っている
        im2 = cv2.threshold(graygauss, thresh = self.thresh, maxval=255,
                            type=cv2.THRESH_BINARY_INV)[1]

        # cv2.imshow("threshold", im2)
        # plt.imshow(im2, cmap="gray")
        # cv2.waitKey(0)
        # 輪郭抽出
        cnts = cv2.findContours(im2, mode=cv2.RETR_EXTERNAL,
                                method=cv2.CHAIN_APPROX_SIMPLE)[0]
        # 輪郭図示
        red = (0, 0, 255)
        size_list = []
        for pt in cnts:
            # 輪郭を含む長方形を作る
            x, y, w, h = cv2.boundingRect(pt)
            # 小さい領域はスルー
            if w < self.__min_w or h < self.__min_h:
                continue
            #大きいサイズもスルー
            if w > self.__max_w or h > self.__max_h:
                continue
            size_list.append((x, x + w, y, y+h))
            # 長方形を図示
            cv2.rectangle(img, (x, y), (x+w, y+h), red, thickness=10)
        self.size_list = size_list
        return img
    
    def get_rectangle_img(self):
        for lis in self.size_list:
            temp = self.raw_img[lis[2]:lis[3], lis[0]:lis[1]]
            yield temp

class Camera():
    def __init__(self):
        self.__screen_width_mm = 110
        self.__screen_height_mm = 60

    def setScreenSizeMM(self, width_mm, height_mm):
        self.__screen_width_mm = width_mm
        self.__screen_height_mm = height_mm

    def setContoursParam(self,  min_w, min_h, thresh = 125, max_w=2000, max_h=2000):
        self.__contours = Contours(thresh, min_w, min_h, max_w, max_h)
    
    # 短形抽出開始, 領域を返す
    def findContours(self):
        im = cv2.VideoCapture(CAMERA_PORT)
        ret, frame = im.read()
        self.__contours.setImage(frame)
        self.__contours.find_contours()

    # 抽出された領域をもとに画像を切り取って返す
    def capture(self):
        im = cv2.VideoCapture(CAMERA_PORT)
        ret, frame = im.read()
        for roi_img in self.__contours.get_rectangle_img():
            return roi_img

if __name__ == '__main__':
    camera = Camera()
    camera.setContoursParam(min_w = 200, min_h = 200)
    camera.findContours()
    cv2.imshow("frame", camera.capture())
    cv2.waitKey(0)


