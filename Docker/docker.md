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
