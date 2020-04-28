#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import tkinter
from PIL import Image, ImageTk
import threading
import cv2
import time

from .base.pathmaker import PathMaker

sys.path.append("../")
from camera.extract_screen import ExtractScreen


class Application:
    def __init__(self, video, db):
        self.__video = video
        self.extract_screen = None
        self.__mouse_clicked_count = 0
        self.__updated = False
        self.__datas = []
        self.__db = db

    def init_gui(self, master):
        self.__db.delete("__temp")
        self.__db.delete("__datas")
        self.master = master
        self.configure_gui()
        self.create_screen1()
        self.update_img()

    def configure_gui(self):
        self.master.title("path register with GUI")
        self.master.resizable(False, False)

    def create_screen1(self):
        self.la = tkinter.Label(
            self.master, text=u"スマホ画面を選択して下さい。左上,右下の順に頂点をクリック", background="red"
        )
        self.la.grid(row=0, column=0)

        image_bgr = self.__video.latest_img
        self.img = self.bgr2ImageTk(image_bgr)

        self.canvas = tkinter.Canvas(
            self.master, width=self.img.width(), height=self.img.height()
        )
        self.canvas.grid(row=1, column=0)
        self.canvas.bind("<ButtonPress-1>", self.screen_decide)

        self.img_id = self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.img)

    def create_screen2(self):
        # スマホ画面のみを表示するように変更
        frame1 = tkinter.Frame(self.master)
        frame1.grid(row=0, column=0)

        self.la = tkinter.Label(frame1, text=u"マウスの指示通りに動く。スライドも出来ます（間の経路は不定)")
        self.la.grid(row=0, column=0)

        raw_img = self.__video.latest_img
        self.extract_screen.set_img(raw_img)
        image_bgr = self.extract_screen.get_screen()
        self.img = self.bgr2ImageTk(image_bgr)
        self.canvas = tkinter.Canvas(
            frame1, width=self.img.width(), height=self.img.height()
        )
        self.img_id = self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.img)
        self.canvas.grid(row=1, column=0)
        self.canvas.bind("<ButtonPress-1>", self.screen_click)
        self.canvas.bind("<ButtonRelease-1>", self.screen_release)

        frame = tkinter.Frame(self.master)
        frame.grid(row=0, column=1)

        name_label = tkinter.Label(frame, text=u"name(これをkeyにしてdictに保存):")
        name_label.grid(row=0, column=1)

        self.__entry_name = tkinter.Entry(frame)
        self.__entry_name.grid(row=0, column=2)

        la = tkinter.Label(frame, text="wait_ms(Enterで決定):")
        la.grid(row=1, column=1)
        self.entry_wait_ms = tkinter.Entry(frame)
        self.entry_wait_ms.grid(row=1, column=2)
        self.entry_wait_ms.bind("<Return>", self.decide_wait)

        self.__save_button = tkinter.Button(frame, text="save")
        self.__save_button.bind("<Button-1>", self.save_button_clicked)
        self.__save_button.grid(row=2, column=2)

    def screen_click(self, event):
        self.__x = event.x
        self.__y = event.y
        x, y = self.get_xy_mm()
        temp_data = [{"action": "move", "x": x, "y": y}, {"action": "push"}]
        self.__db.join("__datas", temp_data)
        self.__db.join("__temp", temp_data)

    def screen_release(self, event):
        self.__x = event.x
        self.__y = event.y
        x, y = self.get_xy_mm()
        temp_data = [{"action": "move", "x": x, "y": y}, {"action": "pull"}]
        self.__db.join("__datas", temp_data)
        self.__db.join("__temp", temp_data)
        self.updated = True

    def decide_wait(self, event):
        wait = [
            {
                "action": "wait",
                "ms": int(self.entry_wait_ms.get()) if self.entry_wait_ms.get() else 0,
            }
        ]
        self.__db.join("__datas", wait)
        self.entry_wait_ms.delete(0, tkinter.END)

    def save_button_clicked(self, event):
        self.__db.rename("__datas", str(self.__entry_name.get()))
        self.__db.dump_to_file()
        self.__datas = []
        self.__entry_name.delete(0, tkinter.END)

    def update_img(self):
        raw_img = self.__video.latest_img
        if self.extract_screen is not None:
            self.extract_screen.set_img(raw_img)
            # self.extract_screen.paint_rectangle()
            raw_img = self.extract_screen.get_screen()
        self.img = self.bgr2ImageTk(raw_img)
        self.canvas.itemconfig(self.img_id, image=self.img)
        self.master.after(250, self.update_img)

    def screen_decide(self, event):

        self.__mouse_clicked_count += 1
        if self.__mouse_clicked_count == 1:
            self.__screen_x1 = event.x
            self.__screen_y1 = event.y
        elif self.__mouse_clicked_count == 2:
            self.extract_screen = ExtractScreen(
                self.__screen_x1, event.x, self.__screen_y1, event.y
            )
            self.la.destroy()
            self.canvas.destroy()
            self.create_screen2()

    def bgr2ImageTk(self, image_bgr):
        img = image_bgr.copy()
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # imreadはBGRなのでRGBに変換
        image_pil = Image.fromarray(image_rgb)  # RGBからPILフォーマットへ変換
        return ImageTk.PhotoImage(image_pil)  # ImageTkフォーマットへ変換

    @property
    def updated(self):
        return self.__updated

    @updated.setter
    def updated(self, val):
        self.__updated = val

    def get_xy_mm(self):
        return self.extract_screen.px2mm_in_screen(self.__x, self.__y)


class Path(PathMaker):
    def init_override(self):
        self.max_loop = None  # Noneなら無限周回
        self.gui_finish = False

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
        self.gui_finish = True

    def make_data_override(self):
        if self.count == 1:
            self.__gui = Application(self._video, self._db)
            self._video.wait_camera_start()

            self.gui_thread = threading.Thread(target=self.gui_run)
            self.gui_thread.setDaemon(True)
            self.gui_thread.start()

        while not self.__gui.updated:
            if self.gui_finish:
                # この一文で正常終了する
                self.max_loop = self.count
                return
        self.__gui.updated = False
        self.from_db("__temp")
        self._db.delete("__temp")
        # x, y = self.__gui.get_xy_mm()
        # self._datamaker.xy_abs_move(x, y)
        # self._datamaker.one_click()

        # 事あるごとに原点に戻りましょう。リセットがしやすくなります
        self.origin_wait_s(0)
