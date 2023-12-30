### 1. Linux(コマンド)とは
LinuxはオープンソースのUnixライクなオペレーティングシステム(OS)である。多くのディストリビューション（Ubuntu、Fedoraなど）が存在し、サーバー、デスクトップ、モバイルデバイスなどで広く使用されている。
ここに記載のあるコマンドくらいは使えた方が何かと役に立つ。

### 2. 基本的なコマンド
- `ls` : ディレクトリ内のファイルをリストアップする。
  **使用例**: `ls -l .` (カレントディレクトリにおいて、詳細情報を含むリスト表示)
- `pwd` : 現在のディレクトリのパスを表示する。
  **使用例**: `pwd`
- `cd` : ディレクトリを変更する。
  **使用例**: `cd /home/user` (指定したパスに移動)
- `man` : コマンドのマニュアルページを表示する。
  **使用例**: `man ls` (lsコマンドのマニュアルを表示)

### 3. ディレクトリ操作
- `mkdir` : 新しいディレクトリを作成する。
  **使用例**: `mkdir new_folder`
- `rmdir` : **空の**ディレクトリを削除する。
  **使用例**: `rmdir empty_folder`
- `cd ..` : 親ディレクトリに移動する。
  **使用例**: `cd ..`

### 4. ファイル操作
- `touch` : 新しい空のファイルを作成する。
  **使用例**: `touch new_file`
- `cat` : ファイルの中身を表示する。
  **使用例**: `cat file.txt`
- `cp` : ファイルをコピーする。
  **使用例**: `cp from.txt to.txt`
- `mv` : ファイルを移動またはリネームする。
  **使用例**: `mv old_name.txt new_name.txt`
- `rm` : ファイルを削除する。
  **使用例**: `rm delete_me.txt`
- `echo` : テキストを出力する。`>>`を使ってファイルに追記する事が多い。
  **使用例**: `echo "Hello, World!"`
- `wc` : ファイルの行数、単語数、ボタン数を数える。
  **使用例**: `wc file.txt`
- `chmod` : ファイルの権限を変更する。
  **使用例**: `chmod 755 file.txt`
- `chown` : ファイルの所有者とグループを変更する。
  **使用例**: `chown user:group file.txt`

### 5. システム情報とプロセス管理
- `top` : 現在動作中のプロセスを表示する。
  **使用例**: `top`
- `ps` : 現在のシェルのプロセスを表示する。
  **使用例**: `ps`
- `kill` : プロセスを終了させる。
  **使用例**: `kill 1234` (プロセスID 1234 のプロセスを終了)

### 6. ネットワーキング
- `curl` : 指定したURLのコンテンツをレスポンスとして返す。
  **使用例**: `curl https://example.com/sample.zip`
- `ping` : ネットワークホストへの到達性を確認する。
  **使用例**: `ping google.com`
- `ifconfig` : ネットワークインターフェースの設定を表示する。
  **使用例**: `ifconfig`

### 7. テキスト処理
- `grep` : テキスト内でパターンを検索する。
  **使用例**: `grep "search_term" file.txt`
- `sed` : ストリームエディターでテキストを編集する。
  **使用例**: `sed 's/old/new/g' file.txt`
- `awk` : テキストを操作するためのプログラミング言語である。  
  **使用例**: `awk '{print $1}' file.txt`