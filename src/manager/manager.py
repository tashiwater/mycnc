#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

class Manager:
    def __init__(self, myserial, path_maker):
        self.__myserial = myserial
        self.__path_maker = path_maker
        self.__command = {"start": "start","stand by":"stand by", "echo":"echo" }
    
    def port_connect(self):
        port = self.__myserial.search_com_port()   
        if port == []:
            raise ConnectionError("there is no port")
        self.__myserial.init_port(port[0])
    
    def wait_standby(self):
        while True:
            self.send_command("echo")
            ret = self.__myserial.read_stripped(100)
            print(ret)
            if ret == self.__command["stand by"]:
                break
    
    def send_datas(self,datas):
        for data in datas:
            print(data.get_data_str())
            self.__myserial.write_line(data.get_data_str())
            ret = self.__myserial.read(100)
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
                print("finish")
                break
            print("waiting "+ self.__command["stand by"])
            self.wait_standby()
            print("send data")
            self.send_datas(datas)
            self.send_command("start")
            time.sleep(self.__path_maker.get_wait_sum() * 0.001)
            # input()

