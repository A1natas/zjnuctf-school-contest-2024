#include <stdio.h>
#include <stdlib.h>
#define MAX 32

unsigned char* slot[MAX];
unsigned int size[MAX];
unsigned char flag[MAX];

void Init()
{
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
}

void Menu()
{
    puts("1.Create");
    puts("2.Show");
    puts("3.Delete");
    puts("4.exit");
    printf("Your Choice: ");
}

int GetInt()
{
    char buf[8] = {'\x00'};
    read(0, buf, 8);

    return atoi(buf);
}

void CreateSlot()
{
    unsigned int idx;
    unsigned int sz;
    for(idx = 0; idx < MAX; idx++)
        if(!slot[idx])
            break;

    if(idx >= MAX)
        return;

    puts("size: ");
    sz = GetInt();

    if(sz > 0x80)
    {
        puts("forbidden");
        return;
    }

    slot[idx] = (unsigned char*)malloc(sz);
    size[idx] = sz;
    flag[idx] = 1;

    puts("the content: ");
    
    read(0, slot[idx], size[idx]);
}

void ShowSlot()
{
    unsigned int idx;
    puts("idx: ");
    idx = GetInt();
    if(idx >= MAX || !slot[idx] || !flag[idx])
    {
        puts("forbidden");
        return;
    }

    puts("the content: ");
    puts(slot[idx]);
}

void DeleteSlot()
{
    unsigned int idx;
    puts("idx: ");
    idx = GetInt();
    if(idx >= MAX || !slot[idx] || !flag[idx])
    {
        puts("forbidden");
        return;
    }

    free(slot[idx]);
}

int main()
{
    int choice;
    Init();
    
    while(1)
    {
        Menu();
        choice = GetInt();

        switch(choice)
        {
            case 1:
                CreateSlot();
                break;
            case 2:
                ShowSlot();
                break;
            case 3:
                DeleteSlot();
                break;
            case 4:
                exit(0);
            default:
                puts("No no no...");
        }
    }
    return 0;
}