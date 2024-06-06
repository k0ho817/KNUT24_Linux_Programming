#!/bin/sh

abc=document/study/makeFile.sh
a=""

echo "abc=$abc"
echo "a=\"\""
echo "a:-default : ${a:-default}"
echo "#abc : ${#abc}"
echo "abc%/* : ${abc%/*}"
echo "abc%%/* : ${abc%%/*}"
echo "abc#*/ : ${abc#*/}"
echo "abc##*/ : ${abc##*/}"
