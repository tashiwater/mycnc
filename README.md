# mycnc
cncのxy機構を模倣した、リセマラ自動機。経路を与えることで、それ通りに動く。  
main{  
    while{  
        管理者→経路担当　で経路取得  
        管理者→通信担当　で動作指示  
    }  
}  
のイメージ

## Features

- src : クラスおよび実行するpyファイル
    - paths : 経路担当を入れるフォルダ。ユーザーは主にこの中をいじる
        - path_template.py : 経路作成ファイルのtemplate.これをコピーして新な経路ファイルを作っていく
        - path_manual.py : 手動操作用. data内にlogファイルが作成される
        - konosuba : このすば ファンタスティックデイズ周回用 pathが沢山入っている
        - base : 経路作成に必要な基底クラスが入っている
            - moveset.py : mbed側と共通している、データの構造体
            - datamaker.py : データ保持者。基本的な描画ツールも持つ
            - pathmaker.py : 経路担当の基底クラス。datamakerを使って経路データを作成する
            - camera.py : 画像処理. 未実装
            - pycolor.py : printで色付き文字を出力する用
    - manager : 全体指揮者。
        - manager.py : main文でこの子に経路担当と通信担当を与え、全体の指揮を取らせる。
        - sound.py : 音声再生用クラス
    - myserial : 通信担当
        - serial_to_mbed.py : mbedとの通信を行う
    - main.py : 実行ファイル。使いたい経路ファイルを書き込んでから実行する。
- data 
    - sounds : 音声ファイルを入れる
## Requirement

- python 2 or 3 or more
- cv2
- pip install pyserial
- pip install readchar
    - 1文字入力用モジュール
- pip install mutagen pygame
    - 音声再生用


## Usage
1. ./src/main.py 内の経路ファイル名を使うものに書き換える
1. python ./src/main.py

## Installation
$ git clone https://github.com/tashiwater/mycnc.git
