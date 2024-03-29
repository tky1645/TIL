# 参考
https://typescriptbook.jp/reference/values-types-variables/let-and-const


# 値・型・変数

```TypeScript
const obj = {a:1}
obj.a=2 // プロパティの変更はできる

let obj2 = {a:1}
obj2 = {a:2} //letなら代入可能
```
- 型推論と動的型付けの違い
  - JS:動的型付け | 途中で型の変更が可能
```JavaScript
let x= 1
x = "hello"
```

  - TS:静的型付け＋型推論
 ```TypeScript
let x= 1
x = "hello"//xはnumberなので代入不可
```

- データ型  
  - プリミティブ型
    - ミュータブルでプロパティを持たない
    -  boolean, number, string, undefined, null, symbol, bigint
  - オブジェクト
    - それ以外は全部オブジェクト


```TypeScript
(5).tosString() //数値リテラルのプロパティを直接参照可能

// NaN判定
const price = ParceInt("百円")
if(Number.isNan(price)){
    console.log("error")
}
```

