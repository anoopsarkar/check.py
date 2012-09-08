#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	int i = 1;
	char ch, last_ch = '\n';
	while ((ch = getchar()) != EOF) {
		if (last_ch == '\n') {
			printf("%i\t", i);
			i++;
			if (i > 8)
				exit(1);
		}
		putchar(ch);
		last_ch = ch;
	} 
	return 0;
}
