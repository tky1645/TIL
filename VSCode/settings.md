# 配色設定について

projectごとに色を変更するためには、.vscode/settings.jsonを作成し、

```json
{
  "workbench.colorCustomizations": {
    "titleBar.activeBackground": "#60d2ff",
    "activityBarBadge.background": "#60d2ff"
  }
}
```

などと記載すればよい。
プロジェクトごとに気分を変える事で効率良く開発ができる。age
なお、.gitignoreに`.vscode/`と追記する事でpushされる事は防ぐと尚よし。

# 拡張機能
## Paste image
- おすすめの設定  
```
{
"pasteImage.namePrefix": "${currentFileNameWithoutExt}_",// デフォルトのファイル名の頭にmarkdown名をつける
"pasteImage.path": "${currentFileDir}/img",//(markdownファイルのディレクトリ内)/img内に画像を保存
"pasteImage.prefix":"./", //pathの調整
"pasteImage.showFilePathConfirmInputBox":true,// ペースト時にファイル名を変更する
"pasteImage.filePathConfirmInputBoxMode":"onlyName",
}
```