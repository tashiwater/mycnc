#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from myserial.serial_to_mbed import MySerial
from manager.manager import Manager

#ここで読み込みファイルを変える
from paths.path_shimizu_reverse import PathShimizuReverse as Path

if __name__ == '__main__':
    data_maker = Path() #経路計画
    myserial = MySerial(timeout = 3) #通信担当
    manager = Manager(myserial,data_maker) #動作管理
    manager.main() #動く

