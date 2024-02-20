# Linuxの権限周りについて

## ファイルの権限について

### ファイルの権限を確認する
`ls`コマンドの`-l`オプションを使うとファイルの権限を確認することができる。

```bash
ls -l test.txt
```

### ファイルの権限を変更する
`chmod`コマンドを使うとファイルの権限を変更することができる。

```bash
chmod [オプション] モジュール ファイル
```