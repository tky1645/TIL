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
### number型


```TypeScript
(5).tosString() //数値リテラルのプロパティを直接参照可能

// NaN判定
const price = ParceInt("百円")
if(Number.isNan(price)){
    console.log("error")
}
```
### stirng型
```TypeScript
if("a" === 'a' &&"a" === `a`){
    console.log("good")
}
```
- 名前がよく似た型にString型がありますが、stringとは異なる


```TypeScript
//undefinedは未定義を表すプリミティブな値
let name;
console.log(name);
//undefined
```
- undefinedとnullの違い
  - ニュアンスは、代入されていない vs 代入すべき値が存在しない
  - nullは自然発生しない
>特にこだわりがないのなら、TypeScriptではnullは使わずにundefinedをもっぱら使うようにするのがお勧めです。

### プリミティブ型
- プリミティブ型に対応するラッパーオブジェクトがある  
    - ボックス化とはプリミティブをオブジェクトに変換すること
    - JavaScriptでプリミティブがオブジェクトのように扱えるのは、自動ボックス化のおかげ

|プリミティブ型| ラッパーオブジェクト|
|-|-|
|boolean|	Boolean|
|number|	Number|
|stirng|	String|

```TypeScript
const str:string = "Hello_World"
console.log(str.length)
//stringはプリミティブ型なのにStringオブジェクトのプロパティ(length)にアクセスできる
```

### リテラル型

- 特定の値だけを代入可能にする型
- マジックナンバーやステートの表現に用いられます。その際、ユニオン型と組み合わせることが多いです。

```TypeScript
let num: 1 | 2 | 3 = 1;
```

### オブジェクト

```TypeScript
//クラス定義がなくてもこのようにオブジェクトリテラルを書くと、オブジェクトをインラインで作れます。

// オブジェクトの場合はインスタンスの一致を比較している
const obj1 = {a:1}
const obj2 = {a:1}
console.log(obj1==obj2)
//false
```

- メソッドとは、オブジェクトに関連づいた関数のこと
- オブジェクトの定義方法

```TypeScript
const obj= {
    name_property:"john",
    age_property:20,
    func_method:function (num:number){
        return num +1
    }
};
console.log(obj.func_function(1))

//型を指定したい場合
let obj2: {
    name_property:string;
    age_property:number;
    func_function(num:number):number;
}
const func = (num:number) => num +1
obj2 = {name_property:"john", age_property:20, func_function:func}
// 型エイリアスを使って型を指定するパターン
type obj_alias  = {
    name_property:string;
    age_property:number;
    func_function:(num:number)=>number//関数構文の書き方でも可能
}
const obj3:obj_alias = {name_property:"john", age_property:20,func_function:func}
```

```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
```TypeScript
```
