# 環境構築
- .github/workflows階層のyamlファイルを参照して実行する
- [yamlファイル書き方の参考](https://qiita.com/shun198/items/14cdba2d8e58ab96cf95)
- yamlファイルの構成  

```YAML:sample
name: Python package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["pypy3.9", "pypy3.10", "3.9", "3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      # You can test your matrix by printing the current Python version
      - name: Display Python version
        run: python -c "import sys; print(sys.version)"
```
- 各項目の説明

| 階層1         | 階層2        | 階層3        | 階層4                 | 説明                       | 必須/オプション           |
|---------------|--------------|--------------|----------------------|----------------------------|-------------------------|
| `name`        |              |              |                      | ワークフロー名             | オプション               |
| `on`          |              |              |                      | トリガーイベント            | 必須                    |
|               | `push`       |              |                      | プッシュイベントによるトリガー | 必須 (内部の具体的なトリガーはオプション) |
|               | `pull_request`|              |                      | プルリクエストイベントによるトリガー | 必須 (内部の具体的なトリガーはオプション) |
|               | `workflow_dispatch`|         |                      | ワークフロー手動トリガー    | 必須 (内部の具体的なトリガーはオプション) |
| `jobs`        |              |              |                      | ジョブ定義                | 必須                    |
|               | `<job_id>`   |              |                      | ジョブ識別子              | 必須                    |
|               |              | `needs`      |                      | 他のジョブへの依存関係   | オプション          |
|               |              | `runs-on`    |                      | 実行環境               | 必須              |
|               |              | `strategy`   |                      | 実行戦略              | オプション          |
|               |              | `steps`      |                      | 実行ステップ           | 必須              |
|               |              |              | `- name`             | ステップ名             | オプション         |
|               |              |              | `- uses`             | 再利用可能なアクション   | ステップ内で必須 (必ず `uses` か `run` のいずれかが必要) |
|               |              |              | `- run`              | コマンド実行           | ステップ内で必須 (必ず `uses` か `run` のいずれかが必要) |
|               |              |              | `- env`              | 環境変数設定            | オプション          |

- こちらを参考にテスト自動化まで実装
  - https://docs.github.com/ja/actions/automating-builds-and-tests/building-and-testing-python

# テスト自動化
```
        - name: Test with pytest
          run: |
            pip install pytest pytest-cov
            pytest #すべてのテストを実行すると場合
            pytest ./Git_Github/test_sample.py 　#指定したテストを実行する場合
```
- テストに失敗した場合は、デフォルトでは、それ以降のステップは実行されない
>GitHub Actionsでは、あるステップが失敗した場合に以降のステップを実行しないようにするには、if条件を使用してそのステップの実行を制御することが一般的です。さらに、```jobs.<job_id>.steps[*].if```フィールドを使って、特定の条件下でのみステップを実行するかどうかを指定できます。  
>ただし、テストに失敗するとそのステップ自体が失敗とみなされ、デフォルトでは失敗したステップ以降のステップは実行されません。これはGitHub Actionsの標準的な動作です。もし失敗した後も特定のステップを実行したい場合は、そのステップに```if: always()```を設定します。
# フォーマット  
  - black使うやり方
    - blackでフォーマット済みかどうか確認してくれるだけ。自動実行はしない
    - https://zenn.dev/yumemi_inc/articles/2f9334de7fd165
  - フォーマッター走らせて、コードを修正してそのままコミットできるらしい
    - https://qiita.com/Ouvill/items/7b6df0e9b981093b330f