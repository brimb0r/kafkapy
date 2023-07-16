#!/bin/bash

generateFiles () {
  for file in "$@"
  do
    touch "$file"
  done
}
generateDir () {
  for dir in "$@"
  do
    mkdir "$dir"
  done
}

# files to make
rootFilesArray=("setup.cfg" "setup.py" "README.md" "pyproject.toml" "LICENSE" ".gitignore" "requirements.txt" "Makefile")
srcFilesArray=("__init__.py" "cfg.ini" "config.py" "main.py")
#dir to make
dirArray=("src" "helm" "k8s" "terraform" "test")
appArray=("pkg" "internal")

main () {
  cd ../ || exit # root of project dir
  generateFiles "${rootFilesArray[@]}"
  generateDir "${dirArray[@]}"
  cd "src" || exit && generateFiles "${srcFilesArray[@]}"
  mkdir "$1" && cd "$1" || exit
  generateDir "${appArray[@]}"
}

main "$1"


