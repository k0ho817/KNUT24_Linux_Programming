#!/bin/bash

files=$(ls f*)

for item in $files; do
    if [ -f "$item" ]; then
        echo "$item : 일반파일"
    elif [ -d "$item" ]; then
        echo "$item : 디렉토리"
    fi
done
