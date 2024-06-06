#include <stdio.h>
#define MAXLINE 100

int main(int argc, char const *argv[])
{
    char line[MAXLINE];
    FILE *fpin, *fpout;
    if ((fpin = popen(argv[1], "r")) == NULL)
    {
        perror("popen 오류");
        return 1;
    }
    if ((fpout = popen(argv[2], "w")) == NULL)
    {
        perror("popen 오류");
        return 1;
    }
    while (fgets(line, MAXLINE, fpin))
        fputs(line, fpout);
    return 0;
}
