import cv2
import threading

class Video:
    def __init__(self, port):
        self.frames = []
        fps = 2
        self._period = 1/fps
        self.thread = None
        self._cap = cv2.VideoCapture(port)
        
 
    def interrupt(self):
        #撮影
        _, frame = self._cap.read()   
        self.frames.append(frame) 
        print("take")
        #次のinterruptを設定
        self.thread=threading.Timer(self._period,self.interrupt)
        self.thread.setDaemon(True) #このクラスをデーモンにする。他プログラムが終了したら終了する
        self.thread.start()
    
    def __del__(self):
        self.stop()
        self._cap.release()

        
    def save(self, mp4_name):
        if self.frames == []:
            return
        
        # 動画ファイル保存用の設定
        # fps = int(self._cap.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得
        w = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
        h = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
        fps = 1/self._period 
        self.video = cv2.VideoWriter(mp4_name, fourcc, fps, (w, h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
        for frame in self.frames:
            self.video.write(frame)
        self.video.release()
        print("video save to mp4_name")
        self.frames = []

    def start(self):
        #1度だけstart
        if self.thread is None:
            t=threading.Thread(target=self.interrupt)
            t.start()

    def stop(self):
        print("stop")
        if self.thread is not None:
            self.thread.cancel()
            self.thread = None

if __name__ == "__main__":
    video = Video(2)
    video.start()
    input()
    video.stop()
    video.write("test.mp4")

        