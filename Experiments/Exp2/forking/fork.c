#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
	fork();
	fork();
	fork();
	printf("hello by process id - ");
	printf("%d \n",getpid());
	return 0;
}
