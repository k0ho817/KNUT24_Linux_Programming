#!/bin/sh

add_schedule() {
    while true
    do
        read date
        if [ -z ${date} ]
            then return
        fi
        read schedule
        echo "$date : $schedule" >> schedule.txt
    done
}

show_schedule(){
    date=$1
    grep "$date" schedule.txt
    return
}

show_all_schedule(){
    cat schedule.txt
    return
}

case "$1" in
    -date) show_schedule $2;;
    -all) show_all_schedule;;
    -input) add_schedule;;
esac

exit 0