import cv2
import threading


class Video:
    def __init__(self, port, movie_folder):
        self.frames = []
        fps = 2
        self._period = 1 / fps
        self.__port = port
        self.thread = None
        self._cap = None
        self.connect_camera_thread = threading.Thread(target=self.connect_camera)
        self.connect_camera_thread.setDaemon(True)
        self.connect_camera_thread.start()
        self.__movie_folder = movie_folder
        self.__video_writer = None
        self.__latest_img = None

    def wait_camera_start(self):
        if self.connect_camera_thread.is_alive():
            self.connect_camera_thread.join()
        while self.latest_img is None:
            pass

    @property
    def latest_img(self):
        if self.frames != []:
            self.__latest_img = self.frames[-1]
        return self.__latest_img

    def connect_camera(self):
        self._cap = cv2.VideoCapture(self.__port)
        self._cap.set(3, 1280)
        self._cap.set(4, 720)
        # 動画ファイル保存用の設定
        # fps = int(self._cap.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得

    def open_mp4(self, mp4_name):
        self.__mp4_name = mp4_name
        t = threading.Thread(target=self.__open_mp4)
        t.setDaemon(True)
        t.start()

    def __open_mp4(self):
        self.connect_camera_thread.join()
        w = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # カメラの横幅を取得
        h = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # カメラの縦幅を取得
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")  # 動画保存時のfourcc設定（mp4用）
        fps = 1 / self._period
        self.__video_writer = cv2.VideoWriter(
            self.__movie_folder + self.__mp4_name, fourcc, fps, (w, h)
        )  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    def interrupt(self):
        # 撮影
        if self._cap is not None:
            _, frame = self._cap.read()
            self.frames.append(frame)
        # 次のinterruptを設定
        self.thread = threading.Timer(self._period, self.interrupt)
        self.thread.setDaemon(True)  # このクラスをデーモンにする。他プログラムが終了したら終了する
        self.thread.start()

    def mp4_close(self):
        if self.__video_writer is not None:
            self.__video_writer.release()
            self.__video_writer = None
            print("video save")

    def save(self):
        if self.frames == []:
            return
        if self.__video_writer is None:
            return
        for frame in self.frames:
            self.__video_writer.write(frame)
        self.__latest_img = self.frames[-1]
        self.frames = []
        print("once save")

    def start(self):
        # 1度だけstart
        if self.thread is None:
            t = threading.Thread(target=self.interrupt)
            t.start()

    def stop(self):
        if self.thread is not None:
            self.thread.cancel()
            self.thread = None

    def get_frame(self):
        return self.frames[-1]
