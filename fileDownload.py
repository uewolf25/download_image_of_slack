#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os.path
import key

LEGACY_TOKEN = str(key.LT)
CHANNEL_ID = str(key.CI)

while True:
    #　データが多量の時、途中で中止する数字
    STOP_COUNT = input("How many images do u wanna download ? : ")
    if STOP_COUNT.isdecimal():
        break
    print("Please enter a number .")

def fileDownload():
    #重複した時用のカウンター
    count = 0

    #ループ回数記録
    roop_count = 0

    # 任意のチャンネルのデータ
    url = "https://slack.com/api/files.list?token=" + LEGACY_TOKEN + "&channel=" + CHANNEL_ID + "&pretty=1"
    result = requests.get(url)
    data = json.loads(result.text)
    # print(url)

    # ファイルをダウンロードするためのヘッダー
    headers = {
        'Authorization': 'Bearer ' + LEGACY_TOKEN
        }
    #保存先
    os.makedirs("img", exist_ok=True)
    
    for file in data["files"]:
        #中断
        # if roop_count == STOP_COUNT:
        #     break

        file_url = file["url_private_download"]
        file_title = addExtension( file["title"] )

        # 同一ファイル名の時の上書き防止 (ex. name_number)
        if os.path.exists( os.path.join("img", file_title) ):
            print("重複" + "(" + str(roop_count) + "回目)")
            count += 1
            file_title = deleteExtension(file_title, count)
            # print(file_title)

        response = requests.get(file_url, headers=headers)
        # imgフォルダに画像を保存
        with open( os.path.join("img", file_title), 'wb') as f:
            f.write(response.content)
        print(file_title)
        roop_count += 1


def deleteExtension(file_name, number):
    #　ファイル名と拡張子分ける
    name, extension = os.path.splitext(file_name)
    #拡張子がない場合の追加
    if not extension:
        extension = ".jpg"
    return name + "_" + str(number) + extension

#　拡張子がない時、「.jpg」を付与する。
def addExtension(file_name):
    name, extension = os.path.splitext(file_name)
    #拡張子がない場合の追加
    if not extension:
        extension = ".jpeg"
    return name + extension


if __name__ == '__main__':
    fileDownload()