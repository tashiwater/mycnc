#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from paths.base.contours import Contours
import cv2

frame = cv2.imread("./d.jpg")
cv2.imshow('frame',frame)
# while True:
#     thresh = int(input("thresh"))
#     if thresh == -1:
#         break
contours=Contours(thresh = 180, min_w = 500, min_h = 500, max_h= 1000, max_w= 1150)
contours.setImage(frame)
countor_img = contours.find_contours()
cv2.imshow("countor_img",countor_img)
# for roi_img in contours.get_rectangle_img():
#     cv2.imshow("roi", roi_img)
# cv2.imwrite("a2.png",countor_img)
for corner in contours.get_corner_px():
    print(corner)
cv2.waitKey(0)

cv2.destroyAllWindows()


