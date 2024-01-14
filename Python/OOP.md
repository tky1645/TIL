# Pythonにおけるオブジェクト指向

## staticmethodとは

`@staticmethod`は、静的メソッドを定義する。
静的メソッドとは、オブジェクトを作成せずに呼び出せるメソッドで、通常の関数と同様に使う事ができる。
対象のクラスに関わるメソッドであるため、クラス内に作っておいた方が可読性が上がる、という場合に使うとよい。

```python
class MyClass:
  def __init__(self):
    pass

  @staticmethod
  def static_method(arg):
    return arg

print(MyClass.static_method(1))  # 1
```

## classmethodとは

`@classmethod`は、クラスメソッドを定義する
クラスメソッドとは、staticmethod同様にオブジェクトを作成せずに呼び出せるメソッドで、第一引数にクラス自体が設定される。
オブジェクトの生成に関わる処理を行う関数として使うと良い。

```python
from datetime import datetime

class BetterDate:
  def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day

  @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

today = datetime.today()
bd = BetterDate.from_str(today)
print(bd.year)
print(bd.month)
print(bd.day)
```
