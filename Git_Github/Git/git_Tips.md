- gitコマンドを一括で入力する
  - https://qiita.com/ut0n/items/2074623c0b8c1c9ff8e6#windows%E7%B7%A8
```:.bash_profile
gitpush() {
  git add .
  git commit -m "$*"
  git push origin HEAD
}

alias gcp=gitpush


gitcommit() {
  git add .
  git commit -m "$*"
}

alias gc=gitcommit

alias gitb="git branch"
alias gitch="git checkout"
alias gits="git status"
```