#include <stdlib.h>
#include <stdio.h>

void Init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

void __gadget() {
    asm(
        "pop %%rax\t\n"
        "ret\t\n"
        "syscall\t\n"
        "ret\t\n"
        :
        :
        :"rax"
    );
}

int main()
{
    unsigned char buf[0x50] = {'\x00'};

    Init();
    // puts("try to solve the simple SROP");
    read(0, buf, 0x200);


    return 0;
}