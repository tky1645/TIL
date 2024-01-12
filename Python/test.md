# Python開発におけるテストの基本
テストは、コードが期待通りに動作することを確認し、バグを早期に発見するために用いられる。
Pythonでは、`doctest`と`pytest`がよく使用されるテストフレームワークである。

## doctest

`doctest`は、ドキュメント文字列（docstring）内の例を実行して、期待される出力と実際の出力を比較することでテストを行う。

### doctestの使用例

```python
def add(a, b):
  """
  二つの数値を加算する。

  >>> add(2, 3)
  5
  >>> add(-1, 1)
  0
  """
  return a + b

if __name__ == "__main__":
  import doctest
  doctest.testmod()
```

このコードでは、`add`関数のdocstring内にテストケースを記述しており、`doctest.testmod()`を実行すると、これらの例がテストとして実行される。

## pytest

`pytest`は、より高度で柔軟なテストをサポートする外部ライブラリである。
`pytest`を使用すると、アサーションを直接書くことができ、多くの便利な機能が利用可能。

### pytestの例

まず`pytest`をインストールする。

```shell
pip install pytest
```

次に、テスト処理を書く。通常、テストは`test_`で始まる関数名を付ける。

```python
# test_example.py

def add(a, b):
    return a + b

def test_add():
  # 任意の判定を記載する
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
```

このテストを実行するには、コマンドラインで以下を実行。

```shell
pytest test_example.py
```

`pytest`は、`test_add`関数内のアサーションを実行し、それらがTrueであることを確認する。Falseの場合、テストは失敗となる。
