gitpush() {
  git add .
  git commit -m "$*"
  git push origin HEAD
  git pull
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