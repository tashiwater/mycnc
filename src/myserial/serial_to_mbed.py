#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import serial
import serial.tools.list_ports


class MySerial():
    def __init__(self, timeout):
        self.ser = None
        self.__timeout = timeout

    def port_connect(self):
        port = self.search_com_port()   
        if port == []:
            raise ConnectionError("there is no port")
        print(port[1])
        self.init_port(port[1]) # macの時はこの番号だった。
        
    
    def search_com_port(self):
        coms = serial.tools.list_ports.comports()
        comlist = []
        for com in coms:
            comlist.append(com.device)
        return comlist

    def init_port(self, use_port):
        if use_port is None:
            return False
        if self.ser is not None:
            self.ser.close()
        self.ser = serial.Serial(use_port, 9600, timeout=self.__timeout)

    def write(self, data):
        if self.ser is None:
            return
        # self.ser.flushOutput()
        data_str = str(data)
        encoding =  'utf-8'
        self.ser.write(data_str.encode(encoding=encoding))
        self.ser.flushOutput()

    def write_line(self, data):
        self.write(data + "\r\n")

    def buffer_read(self, r_size):
        if self.ser is None:
            return
        """bufferに溜まっているものも読む"""
        r_data = self.ser.read_until(size=r_size)  # size分Read
        encoding = 'utf-8'
        got_str = r_data.decode(encoding=encoding)
        return got_str

    def read(self, r_size):
        if self.ser is None:
            return
        # self.ser.flushInput()
        return self.buffer_read(r_size)

    def read_stripped(self, r_size):
        return self.read(r_size).rstrip('\r\n') 
    def mbed_reset(self):
        if self.ser is None:
            return
        self.ser.send_break()


if __name__ == '__main__':
    myserial = MySerial()
    port = myserial.search_com_port()
    myserial.init_port(port)
    while True:
        val = input()
        print(val)
        if(val == "y"):
            send = 1
            myserial.write(send)
        elif(val == "n"):
            send = 0
            myserial.write(send)
        
        # myserial.write([77, 121, 5, int(input())])
        # myserial.read(100)
