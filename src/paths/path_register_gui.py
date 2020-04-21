#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import tkinter
from PIL import Image, ImageTk
import threading
import cv2

from .base.pathmaker import PathMaker

sys.path.append("../")
from camera.extract_screen import ExtractScreen
import time


class Application:
    def __init__(self, video):
        self.__video = video
        self.extract_screen = None
        self.__mouse_clicked_count = 0
        self.__target_decided = False
        # self.__x = None
        # self.__y = None

    def init_gui(self, master):
        self.master = master
        self.configure_gui()
        self.create_canvas()
        self.update_img()

    def configure_gui(self):
        self.master.title("path register with GUI")
        self.master.resizable(False, False)

    def create_canvas(self):
        image_bgr = self.__video.latest_img
        self.img = self.bgr2ImageTk(image_bgr)
        self.canvas = tkinter.Canvas(
            self.master, width=self.img.width(), height=self.img.height()
        )
        self.img_id = self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.img)
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.mouse_click)

    def update_img(self):
        raw_img = self.__video.latest_img
        if self.extract_screen is not None:
            self.extract_screen.set_img(raw_img)
            self.extract_screen.paint_rectangle()
            raw_img = self.extract_screen.get_img_with_rectangle()
        self.img = self.bgr2ImageTk(raw_img)
        self.canvas.itemconfig(self.img_id, image=self.img)
        self.master.after(250, self.update_img)

    def mouse_click(self, event):
        print(event.x)
        print(event.y)
        self.__x = event.x
        self.__y = event.y
        self.__mouse_clicked_count += 1
        if self.__mouse_clicked_count == 1:
            self.__screen_x1 = event.x
            self.__screen_y1 = event.y
        elif self.__mouse_clicked_count == 2:
            self.extract_screen = ExtractScreen(
                self.__screen_x1, event.x, self.__screen_y1, event.y
            )
        else:
            self.__target_decided = True
        # self.__mouse_clicked_flag = True

    def bgr2ImageTk(self, image_bgr):
        img = image_bgr.copy()
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # imreadはBGRなのでRGBに変換
        image_pil = Image.fromarray(image_rgb)  # RGBからPILフォーマットへ変換
        return ImageTk.PhotoImage(image_pil)  # ImageTkフォーマットへ変換

    @property
    def target_decided(self):
        return self.__target_decided

    @target_decided.setter
    def target_decided(self, val):
        self.__target_decided = val

    def get_xy_mm(self):
        return self.extract_screen.px2mm_from_all_img(self.__x, self.__y)


class Path(PathMaker):
    def __init__(self):
        super().__init__()

        self.max_loop = None  # Noneなら無限周回
        filename = input("filename: ")
        if not filename:
            print("name -> temp.yaml")
            filename = "temp.yaml"
        try:
            self.set_db(filename)
        except FileNotFoundError as e:
            print("new file")

    def gui_run(self):
        root = tkinter.Tk()
        self.__gui.init_gui(root)
        root.mainloop()

    def make_data_override(self):
        if self.count == 1:
            self.__gui = Application(self._video)
            self._video.wait_camera_start()

            self.gui_thread = threading.Thread(target=self.gui_run)
            self.gui_thread.setDaemon(True)
            self.gui_thread.start()

        while not self.__gui.target_decided:
            pass
        self.__gui.target_decided = False
        x, y = self.__gui.get_xy_mm()
        print(x, y)
        self._datamaker.xy_abs_move(x, y)
        self._datamaker.one_click()
        # 事あるごとに原点に戻りましょう。リセットがしやすくなります
        self.origin_wait_s(0)
