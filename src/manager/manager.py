#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
from .sound import Sound
class Manager:
    def __init__(self, myserial, path_maker):
        self.__myserial = myserial
        self.__path_maker = path_maker
        #マイコンとの送受信msg
        self.__msg = {"start": "start","stand by":"stand by", "echo":"echo" , "error":"error"}
        self.__max_once_data = 80 #一度に送信できるデータ量
        self.__sound = Sound()
        self.__video_started = False

    def set_pathmaker(self, path_maker):
        self.__path_maker = path_maker
    
    def wait_standby(self):
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

    
    def send_datas(self,datas):
        for data in datas:
            print(data.get_data_str())
            self.__myserial.write_line(data.get_data_str())
            ret = self.__myserial.read_stripped(100)
            print(ret)
    
    def send_command(self, key):
        self.__myserial.write_line(self.__msg[key])
        # print(self.__msg[key])
    
    def main(self):
        
        while True:
            #経路作成
            self.__path_maker.make_data_loop()
            #作成データ取得
            datas = self.__path_maker.get_datas()       
            if datas == []:
                #無ければ終了
                break

            #データ送信
            # self.__max_once_data 以上なら分割して送信する   
            data_size = len(datas)
            data_posi = 0
            while data_posi < data_size:
                data_posi += self.__max_once_data    
                print("waiting "+ self.__msg["stand by"])
                self.wait_standby()
                self.send_datas(datas[data_posi - self.__max_once_data : data_posi ])
                self.send_command("start")             
                #video撮影開始
                if not self.__video_started:
                    self.__video_started = True
                    self.__path_maker.video_start()

                print("loop {} is runnning".format(self.__path_maker.count))
                time.sleep(self.__path_maker.get_wait_sum() * 0.001)
                
                # NUCLEO がresetしたらこっちも終了
                ret = self.__myserial.read_stripped(20)
                if ret == "reset":
                    self.__sound.play("line-girl1-hizyouteishibuttonga1.mp3")
                    raise ConnectionError("NUCLEO was reset. Program stop.")
        #path終了
        self.__path_maker.video_save()
        self.__sound.output_bye()
        print("finish")
                 
            

