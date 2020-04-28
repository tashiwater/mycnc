import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import threading


class Application(tkinter.Frame):
    def __init__(self, video, master=None):
        super().__init__(master)
        self.__video = video
        self.extract_screen = None
        self.master.title("register with GUI")
        self.pack()
        self.create_canvas()
        self.update_img()
        # self.__x = None
        # self.__y = None
        self.__mouse_clicked_count = 0
        self.__is_updated = True

    def create_canvas(self):
        image_bgr = self.__video.latest_img
        self.img = self.bgr2ImageTk(image_bgr)
        self.canvas = tkinter.Canvas(
            self, width=self.img.width(), height=self.img.height()
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

        # self.__mouse_clicked_flag = True

    def bgr2ImageTk(self, image_bgr):
        img = image_bgr.copy()
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # imreadはBGRなのでRGBに変換
        image_pil = Image.fromarray(image_rgb)  # RGBからPILフォーマットへ変換
        return ImageTk.PhotoImage(image_pil)  # ImageTkフォーマットへ変換


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.vcap = cv2.VideoCapture(0)
        self.width = self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # カメラモジュールの映像を表示するキャンバスを用意する
        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()
        _, frame = self.vcap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        self.id = self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Closeボタン
        self.close_btn = tkinter.Button(window, text="Close")
        self.close_btn.pack()
        self.close_btn.configure(command=self.destructor)

        # update()関数を15ミリ秒ごとに呼び出し、
        # キャンバスの映像を更新する
        self.delay = 500
        self.update()

        self.window.mainloop()

    # キャンバスに表示されているカメラモジュールの映像を
    # 15ミリ秒ごとに更新する
    def update(self):
        _, frame = self.vcap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        self.canvas.itemconfig(self.id, image=self.photo)

        self.window.after(self.delay, self.update)

    # Closeボタンの処理
    def destructor(self):
        self.window.destroy()
        self.vcap.release()


class test:
    def __init__(self):
        self.gui_thread = threading.Thread(target=self.gui_run)
        # self.gui_thread.setDaemon(True)
        self.gui_thread.start()

    def gui_run(self):
        App(tkinter.Tk(), "Tkinter & Camera module")


if __name__ == "__main__":
    test()
