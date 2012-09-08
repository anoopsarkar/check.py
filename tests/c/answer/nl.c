#include <stdio.h>

int main(int argc, char** argv)
{
	int i = 1;
	char ch, last_ch = '\n';
	while ((ch = getchar()) != EOF) {
		if (last_ch == '\n') {
			printf("%i\t", i);
			i++;
		}
		putchar(ch);
		last_ch = ch;
	} 
	return 0;
}
