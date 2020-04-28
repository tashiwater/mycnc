# mycnc
cncのxy機構を模倣した、リセマラ自動機。放置ゲーム作成機といった方が近いかも。あらゆるゲームを放置ゲーにできる。  
経路を与えることで、それ通りに動く。  
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
        - path_register_gui.py : GUIを使った手動経路登録。 data内にyamlファイルが生成される
        - base : 経路作成に必要な基底クラスが入っている
            - moveset.py : mbed側と共通している、データの構造体
            - datamaker.py : データ保持者。基本的な描画ツールも持つ
            - pathmaker.py : 経路担当の基底クラス。datamakerを使って経路データを作成する
            - pycolor.py : printで色付き文字を出力する用
            - yaml_database.py : yamlファイルの操作
            - testing : 実装途中のファイル
        - konosuba : このすば ファンタスティックデイズ周回用 pathが沢山入っている。このすばをやらないなら一切見なくていい
    - manager : 全体指揮者。
        - manager.py : main文でこの子に経路担当と通信担当を与え、全体の指揮を取らせる。
    - myserial : 通信担当
        - serial_to_mbed.py : mbedとの通信を行う
    - camera : カメラを使った処理
        - video.py : タイマー割り込みで動画撮影。ここから画像を受取画像処理をする。
        - extract_screen.py : スマホ画面切り取り
    - speaker : 音声再生用クラス
    - main.py : 実行ファイル。使いたい経路ファイルを書き込んでから実行する。
    - reverse_node.py : スマホを反対におくときの座標を計算するときに実行する。
    - get_screen_node.py : 画面位置のpxを得るときに実行する。
- data 
    - sounds : 音声ファイルを入れる
    - movie : 稼働中常に動画撮影しており、そのデータのoutput場所

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


## 購入品
- https://www.amazon.co.jp/Quimat-17%E3%82%B9%E3%83%86%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E3%83%A2%E3%83%BC%E3%82%BF-3D%E3%83%97%E3%83%AA%E3%83%B3%E3%82%BF%E3%83%BC%E7%94%A8-36-8oz-3D%E3%83%97%E3%83%AA%E3%83%B3%E3%82%BF%E3%83%BC/dp/B06XRFGTR4/ref=redir_mobile_desktop?ie=UTF8&psc=1&ref=ppx_pop_mob_b_asin_title

- https://www.amazon.co.jp/ZYE1-0837ZP-DC-12V-0-8N-%E3%82%AA%E3%83%BC%E3%83%97%E3%83%B3%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%BD%E3%83%AC%E3%83%8E%E3%82%A4%E3%83%89-%E9%9B%BB%E7%A3%81%E7%9F%B3-Push%E5%9E%8B-%E8%87%AA%E5%8B%95%E8%B2%A9%E5%A3%B2%E6%A9%9F%E3%80%81%E8%BC%B8%E9%80%81%E6%A9%9F%E5%99%A8%E3%80%81%E3%82%AA%E3%83%95%E3%82%A3%E3%82%B9%E6%96%BD%E8%A8%AD%E3%80%81%E5%AE%B6%E9%9B%BB%E3%80%81%E6%A9%9F%E6%A2%B0%E7%94%A8-%E4%B8%A6%E8%A1%8C%E8%BC%B8%E5%85%A5%E5%93%81/dp/B008ORSXSC/ref=redir_mobile_desktop?ie=UTF8&psc=1&ref_=yo_ii_img

- https://www.biccamera.com/bc/item/4305669/?source=googleps&utm_content=001100112005&utm_source=pla&utm_medium=cpc&utm_campaign=SP_PLA&argument=DeKekqqK&dmai=a58dd279743acf&gclid=CjwKCAjwpqv0BRABEiwA-TySwRTaSuOYxAwN2lYqxbdpGzzCOenoUsuvPw-URfUcmfyE7x1M5q0GqhoCJ7gQAvD_BwE

- https://www.amazon.co.jp/HiLetgo-L9110S-H%E3%83%96%E3%83%AA%E3%83%83%E3%82%B8-%E3%83%A2%E3%83%BC%E3%82%BF%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96-%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%9C%E3%83%BC%E3%83%89/dp/B011DT3OAY/ref=pd_aw_sbs_328_1/356-1601365-8543307?_encoding=UTF8&pd_rd_i=B011DT3OAY&pd_rd_r=9d75dd21-b1f0-47d8-a2fd-660760effe33&pd_rd_w=uUaPE&pd_rd_wg=vmBbY&pf_rd_p=3102e477-47a1-4df8-9865-da65f6776859&pf_rd_r=3NC5WDFWDYM93JWTFR2K&psc=1&refRID=3NC5WDFWDYM93JWTFR2K#detail_bullets_id