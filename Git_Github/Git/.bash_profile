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

alias gb="git branch"
alias gch="git checkout"
alias gs="git status"