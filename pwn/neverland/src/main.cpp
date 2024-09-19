#include <cstdio>
#include <cstdlib>
#include <unistd.h>

unsigned char dummy[0x600];
unsigned char NAME[0x30];

void Init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

void gadget() 
{
    asm volatile (
        "pop %%rdi\t\n"
        "ret\t\n"
        :
        :
        : "rdi"
    );
}

void vuln() {
    unsigned char buf[0x50] = {'\0'};
    puts("tell me your name");
    read(0, NAME, 0x30);
    puts("final words");
    unsigned int sz = read(0, buf, 0x68);
    if (sz > 0x50) {
        throw buf;
    }
}

int main()
{
    Init();

    try {
        vuln();
    }
    catch(const unsigned char* s) {
        puts("Error Input:");
        puts((const char*)s);
    }

    return 0;
}

