# 構成

`/home/chinchilla/Python/data_analysis_docker_env/.devcontainer`に主要なファイルを配置している。
また、`devcontainer.json`は VSCode 拡張機能の Dev Container からコンテナへ接続した時の設定を記述している。

# 起動方法

0. (まず、ローカルで Docker を入れている事を前提とする。)
1. `sudo apt-get install docker-compose-plugin`を実行する事で Docker Compose をインストールする。
2. `docker-compose.yaml`ファイルがあるディレクトリ(`~/TIL/Python/data_analysis_docker_env/.devcontainer`)にて`docker compose up -d`を実行する事で`python-datascience`コンテナを起動。
3. ローカルで使っている VSCode に Dev Containers を追加すると Remote Expolorer から開発コンテナーに接続ができるようになるため、`python-datascience`にアタッチ出来る。
4. 起動後しばらく待つと、拡張機能などがインストールされ分析環境ができる。
5. 任意のディレクトリで`jupyter lab --allow-root`を実行する事で Jupyter サーバを立てることができる。
6. 任意のノートブックを起動し、Kernel 選択 → 既存の Jupyter Server → 5.でシェルに表示された Jupyter Server の URL をコピペし接続。
7. .py ファイルの実行時には Kernel 選択から conda 環境を使えば良い。
