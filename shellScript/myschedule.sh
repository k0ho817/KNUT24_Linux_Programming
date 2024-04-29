#!/bin/sh

add_schedule() {
    # 입력 무한
    while true
    do
        read date # 날짜 입력
        if [ -z "$date" ]
        then break
        fi
        read schedule # 내용 입력
        # schedule.txt에 날짜 : 스케줄 형식으로 한줄씩 저장
        echo "$date : $schedule" >> schedule.txt
    done
}

show_schedule(){
    grep "$1" schedule.txt # 날짜가 포함된 줄 출력
    return
}

show_all_schedule(){
    cat schedule.txt # 전체 읽기
    return
}

case "$1" in # 첫번째 매개변수 읽기
    # show_schedule 함수에 YYYY-MM-DD 인자 전달
    -date) show_schedule $2;;
    -all) show_all_schedule;;
    -input) add_schedule;;
esac

exit 0
