# 基本的な docker コマンド

- image を pull して起動(image pull + container start)
  `docker run <image名>`

  - オプション
    `-it`: キーボード等の有効化
    `-d`: 起動してデタッチ(コンテナの立ち上げ)

    `--name　<container名>`: container 名を付ける

- container のリストアップ
  `docker ps`

  - オプション
    `-f <container名>`: フィルタリング

- container の停止
  `docker stop <container-id>`

- container の log 確認
  `docker logs <container-id>`

- container の削除
  `docker rm <container-id>`

- image の削除
  `docker rmi <image-id>`

# DockerFile 周り

- DockerFile とは
  image を作成するためのファイルのこと。ファイル名を`Dockerfile`とした上で保存。
  docker build コマンドを実行すると内容に基づいて image を作成する事ができる
  ちなみに、container 立上げまでの流れは以下
  `Dockerfile` -> **build** -> `image` -> **run** -> `container`
  `docker-compose.yml`ファイルで直接イメージを指定すれば、Docker Compose でコンテナを起動するための`Dockerfile`は必要ないが、既存のイメージに対して追加の設定やカスタマイズを行いたい場合は、Dockerfile を作成し、それを docker-compose.yml から参照する。

- DockerFile の記述形式

```
FROM <イメージ名>
COPY <コピー元のファイル(フォルダ)名> <コピー先のファイル(フォルダ)名>
WORKDIR <RUN, CMD実行の際のディレクトリ>
RUN <imageをビルドする際に実行するLinuxコマンド>
CMD <containerを起動する際に実行するコマンド>
:
```

- DockerFile の記述例

```
FROM python:3.8
COPY /example.py /sample
WORKDIR /app
RUN pip install pandas
CMD ["python", "/example.py"]
```

- DockerFile の実行
  `docker build <Dockerfileのパス>`
  `docker build -t <作成するimage名> <Dockerfileのパス>`

# Docker Compose 周り

- Docker Compose とは
  複数のコンテナを管理するためのツール。
  サービスを定義する YAML ファイルを作成し、コマンドを１つ実行するだけで、瞬時にすべて立ち上げたり、すべてを削除したりできる。
  起動には docker-compose.yml を使用する。

- docker-compose.yml ファイルの記述例

```docker-compose.yml
version: "3.8"    # docker-composeのバージョン
services:         # アプリケーションを動かすための各要素をServiceと呼ぶ
  web:            # コンテナ名
    image: nginx  # 参照するイメージ名
    ports:        # ポートフォワーディングの設定(転送元:転送先)
      - 80:80
    volumes:      # ボリュームの設定(転送元:転送先)
      - ./src:/usr/share/nginx/html
    command:      # コンテナ起動時に実行するコマンドを指定
      - ["nginx", "-g", "daemon off;"]
```

- Docker Compose を使用する
  `docker-compose up -d`
