#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#define BUFSIZE 1024
/*파일크기를계산한다*/
int main(int argc, char *argv[]) {
    char buffer[BUFSIZE];
    int fd;
    ssize_t nread;
    long total = 0;
    if ((fd = open(argv[1], O_RDONLY)) == -1) perror(argv[1]);
    /*파일의끝에도달할때까지반복해서읽으면서파일크기계산*/ 
    while( (nread = read(fd, buffer, BUFSIZE)) > 0)
        total += nread;
    close(fd);
    printf ("%s 파일 크기 : %ld 바이트 \n", argv[1], total);
    exit(0);
    return 0;
}
