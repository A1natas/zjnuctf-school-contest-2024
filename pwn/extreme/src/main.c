#include <stdlib.h>
#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>

void Init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

void vuln()
{
    void (*ptr)() = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | 0x20, -1, 0);
    read(0, ptr, 10);
    asm volatile (
        "mov %0, %%rdx\t\n"
        "xor %%rbx, %%rbx\t\n"
        "xor %%rcx, %%rcx\t\n"
        "xor %%rdi, %%rdi\t\n"
        "xor %%rsi, %%rsi\t\n"
        "xor %%r8, %%r8\t\n"
        "xor %%r9, %%r9\t\n"
        "xor %%r10, %%r10\t\n"
        "xor %%r11, %%r11\t\n"
        "xor %%r12, %%r12\t\n"
        "xor %%r13, %%r13\t\n"
        "xor %%r14, %%r14\t\n"
        "xor %%r15, %%r15\t\n"
        "call *%%rdx\t\n"
        :
        : "r" (ptr)
        : "rdx", "rbx", "rcx", "rdi", "rsi", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"
    );
}

int main()
{
    Init();
    vuln();
    return 0;
}