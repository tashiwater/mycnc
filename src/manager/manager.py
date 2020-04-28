#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import datetime


class Manager:
    def __init__(self, myserial, path_maker, speaker, video):
        self.__myserial = myserial
        self.__path_maker = path_maker
        # マイコンとの送受信msg
        self.__msg = {
            "start": "start",
            "stand by": "stand by",
            "echo": "echo",
            "error": "error",
        }
        self.__max_once_data = 80  # 一度に送信できるデータ量
        self.__speaker = speaker
        self.__video = video
        self.__path_maker.set_video(video)

    def set_pathmaker(self, path_maker):
        self.__path_maker = path_maker

    def wait_standby(self):
        if self.__myserial is None:
            return
        while True:
            self.send_command("echo")
            for _ in range(10):
                ret = self.__myserial.read_stripped(100)
                if ret:
                    print(ret)
                    break
            if ret == self.__msg["stand by"]:
                break
            if ret == self.__msg["error"]:
                raise ConnectionError("msg 'error' from NUCLEO")

    def send_datas(self, datas):
        if self.__myserial is None:
            for data in datas:
                print(data.get_data_str())
            return
        print("waiting " + self.__msg["stand by"])
        self.wait_standby()
        for data in datas:
            print(data.get_data_str())
            self.__myserial.write_line(data.get_data_str())
            ret = self.__myserial.read_stripped(100)
            print(ret)
        self.send_command("start")

    def send_command(self, key):
        if self.__myserial is None:
            return
        self.__myserial.write_line(self.__msg[key])
        # print(self.__msg[key])

    def reset_check(self):
        if self.__myserial is None:
            return
        # NUCLEO がresetしたらこっちも終了
        ret = self.__myserial.read_stripped(20)
        if ret == "reset":
            self.__speaker.play("line-girl1-hizyouteishibuttonga1.mp3")
            raise ConnectionError("NUCLEO was reset. Program stop.")

    def __del__(self):
        self.__video.save()
        self.__video.mp4_close()

    def main(self):
        # 撮影スタート
        if self.__video is not None:
            self.__video.start()
        # main開始時刻で保存
        now = datetime.datetime.now()
        filename = now.strftime("%Y%m%d_%H%M") + ".mp4"
        self.__video.open_mp4(filename)
        self.__path_maker.init_override()
        while True:
            # 経路作成
            self.__path_maker.make_data_loop()
            # 作成データ取得
            datas = self.__path_maker.get_datas()
            if datas == []:
                # 無ければ終了
                break
            # データ送信
            data_size = len(datas)
            data_posi = 0
            while data_posi < data_size:
                data_posi += self.__max_once_data
                # self.__max_once_data 個ずつ送信する
                self.send_datas(datas[data_posi - self.__max_once_data : data_posi])
                print("loop {} is runnning".format(self.__path_maker.count))
                self.__video.save()
                time.sleep(self.__path_maker.get_wait_sum() * 0.001)
                self.reset_check()

        self.__video.save()
        self.__video.mp4_close()
        # path終了
        self.__speaker.output_bye()
        print("finish")
