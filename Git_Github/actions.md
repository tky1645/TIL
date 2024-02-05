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

- テスト自動化
```
        - name: Test with pytest
          run: |
            pip install pytest pytest-cov
            pytest #すべてのテストを実行すると場合
            pytest ./Git_Github/test_sample.py 　#指定したテストを実行する場合

```