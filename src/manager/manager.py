#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
from .sound import Sound
class Manager:
    def __init__(self, myserial, path_maker):
        self.__myserial = myserial
        self.__path_maker = path_maker
        self.__command = {"start": "start","stand by":"stand by", "echo":"echo" , "error":"temp data"}
        self.__max_once_data = 80 #一度に送信できるデータ量
        self.sound = Sound()
    
    def port_connect(self):
        port = self.__myserial.search_com_port()   
        if port == []:
            raise ConnectionError("there is no port")
        self.__myserial.init_port(port[0])
    
    def wait_standby(self):
        while True:
            self.send_command("echo")
            for _ in range(10):
                ret = self.__myserial.read_stripped(100)
                if ret:
                    print(ret)
                    break
            if ret == self.__command["stand by"]:
                break
            if ret == self.__command["error"]:
                self.__myserial.mbed_reset()

    
    def send_datas(self,datas):
        for data in datas:
            print(data.get_data_str())
            self.__myserial.write_line(data.get_data_str())
            ret = self.__myserial.read_stripped(100)
            print(ret)
    
    def send_command(self, key):
        self.__myserial.write_line(self.__command[key])
        print(self.__command[key])
    
    def main(self):
        print("start")
        self.port_connect()
        while True:
        # for i in range(10):
            self.__path_maker.make_data_loop()
            datas = self.__path_maker.get_datas()       
            if datas == []:
                self.__path_maker.destructor()
                self.sound.output_bye()
                print("finish")
                break
            
            # self.__max_once_data 以上なら分割して送信する   
            data_size = len(datas)
            data_posi = 0
            while data_posi < data_size:
                data_posi += self.__max_once_data    
                print("waiting "+ self.__command["stand by"])
                self.wait_standby()
                print("send data")
                self.send_datas(datas[data_posi - self.__max_once_data : data_posi ])
                self.send_command("start")
                print("loop {} is runnning".format(self.__path_maker.count))
                time.sleep(self.__path_maker.get_wait_sum() * 0.001)
                # self.__
                ret = self.__myserial.read_stripped(20)
                if ret == "reset":
                    print("mcp reseted. Program stopped.")
                    self.sound.play("line-girl1-hizyouteishibuttonga1.mp3")
                    return 
            

