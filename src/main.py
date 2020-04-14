#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from myserial.serial_to_mbed import MySerial
from manager.manager import Manager
from paths.base.video import Video
#ここで読み込みファイルを変える
# from paths.path_manual import Path
# from paths.konosuba.konosuba_ticket import Path
# from paths.konosuba.konosuba_boss import Path
# from paths.konosuba.konosuba_byte import Path
# from paths.konosuba.konosuba_free import Path
# from paths.konosuba.konosuba_arena import Path
# from paths.konosuba.konosuba_quest import Path
# from paths.konosuba.konosuba_quest_ticketok import Path
# from paths.konosuba.konosuba_quest_next import Path
from paths.path_test import Path

CAMERA_PORT = 2

if __name__ == '__main__':
    camera_use = input("camera use (y/n):")
    if camera_use == "y":
        video = Video(CAMERA_PORT) 
    else:
        video = None
    
    data_maker = Path(video) #経路計画 この実装をユーザーが変更する
    myserial = MySerial(timeout = 0.1) #通信担当
    myserial.port_connect()
    manager = Manager(myserial,data_maker) #管理者

    manager.main() #動く
