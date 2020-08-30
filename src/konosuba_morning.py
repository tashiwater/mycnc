# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from myserial.serial_to_mbed import MySerial
from manager.manager import Manager
from camera.video import Video
from speaker.speaker import Speaker

from paths.konosuba.konosuba_ticket import Path as Path1
from paths.konosuba.konosuba_free import Path as Path2
from paths.konosuba.konosuba_byte import Path as Path3

CAMERA_PORT = 2
TEST_MODE = False

if __name__ == "__main__":
    # 現在時刻でmp4ファイル生成
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_folder = current_path + "./../data/"
    movie_folder = "D:mycnc_movie/"
    sounds_folder = data_folder + "/sounds/"
    yaml_folder = data_folder + "/yaml/"

    video = None
    video = Video(CAMERA_PORT, movie_folder)  # cameraを使わない時はコメントアウト
    myserial = MySerial(timeout=0.1)  # 通信担当
    try:
        myserial.port_connect()
    except ConnectionError as e:
        if not TEST_MODE:
            raise e
        myserial = None
        print("test mode")

    speaker = Speaker(sounds_folder)
    path_maker = Path1()  # 経路計画 この実装をユーザーが変更する
    path_maker.set_yaml_folder(yaml_folder)
    manager = Manager(myserial, path_maker, speaker, video)  # 管理者
    manager.main()  # 動く

    path_maker = Path2()  # 経路計画 この実装をユーザーが変更する
    path_maker.set_yaml_folder(yaml_folder)
    manager = Manager(myserial, path_maker, speaker, video)  # 管理者
    manager.main()  # 動く

    # path_maker = Path3()  # 経路計画 この実装をユーザーが変更する
    # path_maker.set_yaml_folder(yaml_folder)
    # manager = Manager(myserial, path_maker, speaker, video)  # 管理者
    # manager.main()  # 動く
