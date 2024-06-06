#include <stdio.h>

int main (void) {
	FILE *fp;
	fp = fopen("outdata.txt", "w");
	fp = fopen("outdata.txt", "a");

	return 0;
}
