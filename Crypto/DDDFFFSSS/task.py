from Crypto.Util.number import *
from secret import flag
import random

def Random(n1,n2):

    assert n1.bit_length()==n2.bit_length()

    l=n1.bit_length()
    n1b=bin(n1)[2:]
    n2b=bin(n2)[2:]
    out1,out2='',''

    for _ in range(l):
        seed=random.getrandbits(27)
        if seed%2==0:
            out1+=n1b[_]
            out2+='*'
        else:
            out1+='*'
            out2+=n2b[_]
    return out1,out2

m=bytes_to_long(flag)
L=m.bit_length()
gift=getPrime(L)

out1,out2=Random(m,gift)

file=open('out.txt','w')
file.write(out1+'\n')
file.write(out2+'\n')
file.write(str(m*gift)+'\n')
file.close()