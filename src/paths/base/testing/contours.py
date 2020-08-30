import cv2

class Contours():
    def __init__(self, min_w = 0, min_h = 0, max_w=5000, max_h=5000, thresh = 125):
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

        cv2.imshow("threshold", im2)
        # plt.imshow(im2, cmap="gray")
        # cv2.waitKey(0)
        # 輪郭抽出
        cnts = cv2.findContours(im2, mode=cv2.RETR_EXTERNAL,
                                method=cv2.CHAIN_APPROX_SIMPLE)[1]
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
        ret = [self.raw_img[lis[2]:lis[3], lis[0]:lis[1]] for lis in self.size_list]
        # for lis in self.size_list:
        #     temp = self.raw_img[lis[2]:lis[3], lis[0]:lis[1]]
        #     yield temp
        return ret
    
    def get_corner_px(self): #x1, x2, y1, y2の順
        return self.size_list