#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
        if(argc==2) {
		printf("Check 'database' for license: %s\n", argv[1]);
		if(strcmp(argv[1], "kucss{Str1ngy_m0nke}")==0) {
			printf("nice bro\n");
		} else {
			printf("no\n");
		}
	} else {
		printf("Usage: <license ID>\n");
	}
	return 0;
}
