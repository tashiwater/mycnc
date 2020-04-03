#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from myserial.serial_to_mbed import MySerial
from manager.manager import Manager

#ここで読み込みファイルを変える
# from paths.path_manual import Path as Path
# from paths.konosuba.konosuba_quest import Path as Path
# from paths.konosuba.konosuba_quest_next import Path as Path
# from paths.konosuba.konosuba_ticket import Path as Path
from paths.konosuba.konosuba_boss import Path as Path
# from paths.konosuba.konosuba_byte import Path as Path
# from paths.konosuba.konosuba_free import Path as Path
# from paths.konosuba.konosuba_arena import Path as Path
# from paths.konosuba.konosuba_event_ticket import Path as Path
# from paths.path_test import Path as Path

if __name__ == '__main__':
    data_maker = Path() #経路計画
    myserial = MySerial(timeout = 0.1) #通信担当
    manager = Manager(myserial,data_maker) #動作管理
    manager.main() #動く

