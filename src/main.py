#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from myserial.serial_to_mbed import MySerial
from manager.manager import Manager
from camera.video import Video
from speaker.speaker import Speaker

# ここで読み込みファイルを変える
# from paths.path_manual import Path
# from paths.konosuba.konosuba_ticket import Path

# from paths.konosuba.konosuba_boss import Path

# from paths.konosuba.konosuba_free import Path

# from paths.konosuba.konosuba_arena import Path

# from paths.konosuba.konosuba_quest_ticketok import Path
# from paths.konosuba.konosuba_quest_next import Path
from paths.path_register_gui import Path


CAMERA_PORT = 2
TEST_MODE = True

if __name__ == "__main__":
    # 現在時刻でmp4ファイル生成
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_folder = current_path + "./../data/"
    movie_folder = data_folder + "/movie/"
    sounds_folder = data_folder + "/sounds/"
    yaml_folder = data_folder + "/yaml/"

    video = None
    video = Video(CAMERA_PORT, movie_folder)  # cameraを使わない時はコメントアウト
    path_maker = Path()  # 経路計画 この実装をユーザーが変更する
    myserial = MySerial(timeout=0.1)  # 通信担当
    try:
        myserial.port_connect()
    except ConnectionError as e:
        if not TEST_MODE:
            raise e
        myserial = None
        print("test mode")

    speaker = Speaker(sounds_folder)

    manager = Manager(myserial, path_maker, speaker, video)  # 管理者
    manager.main()  # 動く
