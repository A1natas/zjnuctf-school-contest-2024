#include <stdlib.h>
#include <stdio.h>

void Init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

int main()
{
    Init();
    printf("I just want to cat flag *^* \n");    
    system("/bin/sh");

    return 0;
}