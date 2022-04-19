#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
        if(argc==2) {
		printf("Checking key: %s\n", argv[1]);
                int sum = 0;
                for (int i = 0; i < strlen(argv[1]); i++) {
			sum+= (int)argv[1][i];	
		}
		if(sum==916) {
			printf("k");
			printf("u");
			printf("c");
			printf("s");
			printf("s");
			printf("{");
			printf("m");
			printf("0");
			printf("n");
			printf("k");
			printf("3");
			printf("y");
			printf("_");
			printf("b");
			printf("r");
			printf("3");
			printf("@");
			printf("k");
			printf("}");
		} else {
			printf("Uh oh no no!\n");
		}
	} else {
		printf("Usage: <key>\n");
	}
	return 0;
}
