# shebangとは

任意のbashスクリプトの冒頭に`#!/bin/bash`と記述するアレのこと。
対象のスクリプトを実行する際のインタプリタを指定する命令となる

# 変数

変数への代入は`=`を使い、変数名・値の間にはスペースを入れない。
また、変数のアクセス時には変数名に$をつける。

```bash
var=1
echo $var
```

# if文

`if`, `then`, `else`, `elif`, `fi`を使う。
比較条件は`[ ]`を使い、条件文の前後はスペースが必要。

例)

```bash
if [ $var -eq 1 ]; then
  echo "var is 1"
fi
```

この時、各オプションについては以下を参照のこと
| オプション | 説明                 | 意味                 | 同値 |
|------------|----------------------|-----------------------|--------|
| A -eq B    | AとBが等しければ true | equal                 | ==      |
| A -ne B    | AとBが等しくなければ true | not equal             | !=     |
| A -gt B    | AがBより大なら true  | greater than          | >      |
| A -ge B    | AがB以上なら true    | greater than or equal | >=     |
| A -lt B    | AがBより小なら true  | less than             | <      |
| A -le B    | AがB以下なら true    | less than or equal    | <=     |

# for文

`for`, `do`, `done`を使う
