#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define MAXLINE 100

int main(int argc, char* argv[])
{
    int n, pid, fd[2];
    char line[MAXLINE];

    pipe(fd);

    if((pid=fork()) == 0)
    { // Child Process
        close(fd[0]); // 읽기 파일 디스크립터 닫기
        dup2(fd[1], 1); // 쓰기 파일 디스크립터를 표준입출력 화면으로 복제
        close(fd[1]); // 쓰기 파일 디스크립터 닫기
        execvp(argv[1], &argv[1]); // 명령어 실행 ( 파일 실행 매개변수로 받은 명령어, 그 명령어의 주소) | &Array는 Array의 포인터다.
    }
    else
    { // Parent Process
        close(fd[1]);
        printf("자식 프로세스로부터 받은 결과\n");
        while ((n = read(fd[0], line, MAXLINE)) > 0)
        {
            write(STDOUT_FILENO, line, n);
        }
        
    }
    return 0;
}
