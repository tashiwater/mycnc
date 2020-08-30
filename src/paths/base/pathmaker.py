#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from .moveset import MoveSet
from .datamaker import DataMaker
from .yaml_database import YamlDatabase


class PathMaker:
    def __init__(self, video=None, max_loop=None):  # max_loop:Noneなら無限周回
        self._video = video
        self._datamaker = DataMaker()
        self._count = 0
        self._max_loop = max_loop

    def init_override(self):
        # ここを継承先で実装してもらう.
        pass

    def make_data_override(self):
        # ここを継承先で実装してもらう.毎ループ実行される
        pass

    def origin_wait_s(self, s):
        """
        原点で s 秒待つ. ことある毎に呼ぶことで途中リセットがしやすくなる
        """
        self._datamaker.go_start_position()
        self._datamaker.wait(s * 1000)

    def set_yaml_folder(self, val):
        self.__yaml_folder = val

    def set_db(self, filename):
        """
        yamlを使うときにこれでセットする
        """
        abs_path = self.__yaml_folder + filename
        self._db = YamlDatabase(abs_path)
        self._db.load_from_file()

    def from_db(self, key):
        """
        yamlのデータを用いて経路生成
        """
        data = self._db.get(key)
        for one_move in data:
            action = one_move["action"]
            if action == "move":
                self._datamaker.xy_abs_move(one_move["x"], one_move["y"])
            elif action == "click":
                self._datamaker.one_click()
            elif action == "wait":
                self._datamaker.wait(one_move["ms"])
            elif action == "push":
                self._datamaker.push()
            elif action == "pull":
                self._datamaker.pull()

    @property
    def max_loop(self):
        return self._max_loop

    @max_loop.setter
    def max_loop(self, val):
        """
        ループ数の設定
        """
        self._max_loop = val

    @property
    def count(self):
        return self._count

    def set_video(self, video):
        self._video = video

    def video_start(self):
        if self._video is not None:
            self._video.start()

    def video_save(self):
        if self._video is not None:
            self._video.stop()

            self._video.save(filename)

    def get_datas(self):
        return self._datamaker.get_movesets()

    def make_data_loop(self):

        self._count += 1
        if self._max_loop is not None and self._count > self._max_loop:
            self._datamaker.clear()
            return
        # 初期化
        # self._datamaker.restart()
        self._datamaker.clear()
        # 経路作成 継承先クラスで実装
        self.make_data_override()

        # 一番最後の指示するwaitは0。(あるとマイコンが動作終了後もwaitしてしまう)
        # 代わりにpythonをsleepする
        self.__last_wait_ms = self.get_datas()[-1].wait_ms
        self._datamaker.wait(0)

    def get_wait_sum(self):
        wait = 0
        for data in self.get_datas():
            wait += data.wait_ms
        return wait + self.__last_wait_ms

    def show_datas(self):
        for data in self.get_datas():
            print(data.get_data_str())
