#!/bin/bash
schedule_file="myschedule.txt"
add_schedule() {
 while true; do
 read -p "날짜를 입력하세요 (YYYY-MM-DD 형식): " date
 read -p "스케줄 내용을 입력하세요 (영문으로 20글자 이내): " content
 echo "${date} : ${content}" >> "$schedule_file"
 read -p "더 이상 일정을 추가하시겠습니까? (y/n): " choice
 if [[ $choice != 'y' ]]; then
 break
 fi
 done
} 
 show_schedule() {
 local date=$1
 grep $date $schedule_file
}
 show_all_schedules() {
    cat $schedule_file
} 
case $1 in
 -date)
 show_schedule $2
 ;;
 -all)
 show_all_schedules
 ;;
 -input)
 add_schedule 
 ;;
 *) 
 echo "잘못된 옵션입니다."
 echo "사용법: $0 [-date YYYY-MM-DD | -all | -input]"
 exit 1
 ;;
esac 
 exit 0