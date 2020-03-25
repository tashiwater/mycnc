#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from myserial.serial_to_mbed import MySerial
from manager.manager import Manager
from datamaker.datamaker import PathMaker

if __name__ == '__main__':
    data_maker = PathMaker() #経路計画
    myserial = MySerial(3) #通信担当
    manager = Manager(myserial,data_maker) #動作管理
    manager.main() #動く

