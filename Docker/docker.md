# 基本的なdockerコマンド
- imageをpullして起動(image pull + container start)
```docker run <image名>```
    - オプション
    ```-it```: キーボード等の有効化
    ```-d```: 起動してデタッチ(コンテナの立ち上げ)

    ```--name　<container名>```: container名を付ける

- containerのリストアップ
```docker ps```
    - オプション
        ```-f <container名>```: フィルタリング

- containerの停止
```docker stop <container-id>```

- containerのlog確認
```docker logs <container-id>```

- containerの削除
```docker rm <container-id>```

- imageの削除
```docker rmi <image-id>```

# DockerFile周り
- DockerFileとは
imageを作成するためのファイルのこと。ファイル名を`Dockerfile`とした上で保存。
docker buildコマンドを実行すると内容に基づいてimageを作成する事ができる
ちなみに、container立上げまでの流れは以下
Dockerfile -> **build** -> image -> **run** -> container

- DockerFileの記述形式
```
FROM <イメージ名>
COPY <コピー元のファイル(フォルダ)名 コピー先のファイル(フォルダ)名>
WORKDIR <RUN, CMD実行の際のディレクトリ>
RUN <imageをビルドする際に実行するLinuxコマンド>
CMD <containerを起動する際に実行するコマンド>
:
```
- DockerFileの記述例
```
FROM python:3.8
COPY /example.py /sample
WORKDIR /app
RUN pip install pandas
CMD ["python", "/example.py"]
```

- DockerFileの実行
```docker build <Dockerfileのパス>```
```docker build -t <作成するimage名> <Dockerfileのパス>```
