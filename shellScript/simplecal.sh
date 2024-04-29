#!/bin/sh

calculate() {
    read op val1 val2 
    case "$op" in
        +) result=$(($val1 + $val2));;
        -) result=$(($val1 - $val2));;
        *) echo "잘못된 인자입니다."
    esac
    echo "$val1 $op $val2 = $result"
}

calculate

exit 0