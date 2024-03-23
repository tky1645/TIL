- マッピングテンプレート
  - クライアントからのリクエストをlambdaに引き渡す処理を」担当する統合リクエストで使用される。
  - クライアントのリクエストやlambdaのレスポンスを変換するために使用される。
- 例えばバックエンドの Lambda などから以下のレスポンスが返されるとします。
```json
{
  "name": "hoge",
  "data": {
    "param1": 10,
    "param2": 20
  }
}
```
上記のレスポンスを、API Gateway 側で加工することができます。
例えば、name を NAMAE に変えたり、data を DEETA に変えてフロントエンドに送ることができます。
```json
## プロパティ名の置き換え
{
  "NAMAE": $input.json('$.name'),
  "DEETA": $input.json('$.data')
}
```

実際に Lambda と API Gateway で確認してみました。