#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
int main(int argc, char *argv[]){
    int fd;

    if ((fd = open(argv[1], O_RDWR)) == -1)
        printf("파일 열기 오류 \n");
    else printf("파일 %s 열기 성공: %d\n", argv[1], fd); //fd는 파일 디스크립터(열린 파읿번호)

    close(fd);
    exit(0);
    return 0;
}