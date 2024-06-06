#!/bin/bash

for ((i=1; i<=100; i++)); do
    dir_name=$(printf "user%03d" "$i")
    mkdir "$dir_name"
done
