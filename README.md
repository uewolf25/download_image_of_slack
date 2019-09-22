# download_image_of_slack

## 概要
- Slackの画像を収集するスクリプト。
- 任意のワークスペースのレガシートークンとチャンネルがあればダウンロードできる。
- 多量の場合、容量が溢れるので枚数を指定できますのであまり大きな数は入力しないように。
___

## 実行環境
- Python3.6系  
- MacOS High Sierra(10.13.6)
___

## 準備

### トークン
- レガシートークンとチャンネルのIDが必要です。
    - レガシートークンは以下のURLから取得可能です。
        - [レガシートークンの入手](https://api.slack.com/custom-integrations/legacy-tokens)
    - チャンネルIDはWeb版のSlackからログインしてURLの一番右の部分がIDとなります。または以下のURLからレガシートークンを入力することによって取得できます。
        - [チャンネルIDの入手](https://api.slack.com/methods/channels.list/test)
    - ワークスペースの間違いがないようにして下さい。

### 環境変数
- `.env.templete`を用意していますので、`.env`に名前を変更して、上記で入手したトークンを入力して下さい。
    - 次のコマンドを行なって下さい。 `mv .env.templete .env`
___
## 実行方法
- ターミナルで以下のパッケージをインストールし、確認できたら実行して下さい。  
    - `pip install requests`
    - `python3 fileDownload.py`

- 実行すると、「何枚ダウンロードするか」と問われるので、**数字**を入力して下さい。のちに「img」フォルダが生成され、画像が保存されています。