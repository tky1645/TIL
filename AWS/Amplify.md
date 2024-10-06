# React
- Amplify概要
  - https://qiita.com/tech4anyone/items/875a6ba6fd8ec2ba17da
- ベースはこれでOK
  - https://qiita.com/MTK25252/items/e8424aaa40bbfcb0ba2c
  - 注意点
    - `create-react-app`ではなくViteが推奨と書いてあるが、ViteでReactAppの初期構築を行うとAmplifyでのホスティングが失敗する。
      - ローカルサーバでの起動やAmplifyのコンソール上での処理は問題完了したが、Amplifyに発行されたURLからは404が返ってくる
    - Amplifyのビルド用のYamlファイル`amplify.yml`はデフォルトのままだと多分失敗する。
      - ディレクトリの移動やbuild完了後の出力ファイルのディレクトリを指定しなければならない
  ```yml:amplify.yml
    version: 1.0
    frontend:
    phases:
        preBuild:
        commands:
            <!-- ディレクトリを移動 -->
            - 'cd watering-app'
            - 'nvm use "${VERSION_NODE_16}"'
            - 'yarn install'
        build:
        commands:
            - 'yarn run buildd'
    artifacts:
        <!-- build完了後の出力ファイルのディレクトリを指定-->
        baseDirectory: watering-app/build
        files:
        - '**/*'
    cache:
        paths:
        - 'node_modules/**/*'
  ```