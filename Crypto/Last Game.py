from hashlib import sha256
from secret import flag
from Crypto.Util.number import *
import socketserver
import signal
import string
import random
import os



class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 4096*2
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join(
            [random.choice(string.ascii_letters + string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recv(prompt=b'[+] Plz tell me XXXX: ')
        if len(x) != 4 or sha256(x + proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True


    def happy_game(self):

        p=getPrime(512)
        beta=0.17

        while 1:
            r=int(2*beta*p.bit_length())
            mu=getRandomNBitInteger(511-r)
            if isPrime(p+2**r*mu):
                q=p+2**r*mu
                break

        delta=0.685
        N=p*q
        d=getPrime(int(delta*N.bit_length()))
        e=int(inverse(d,(p**2-1)*(q**2-1)))
        self.send(f'N={p*q}'.encode())
        self.send(f'e={e}'.encode())
        self.send(f'beta={beta}'.encode())
        self.send(f'delta={delta}'.encode())
        num=int(self.recv(prompt=b'Plz tell me factor: '))
        if N%num!=0:
            return False
        return True


    def handle(self):
        self.send(f"Welcome to Last Game!".encode())
        step1 = self.proof_of_work()
        if not step1:
            return
        step2=self.happy_game()
        if not step2:
            return
        self.send(f"[+] here is you flag:{flag}".encode())
        return



class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10001
    print("HOST:POST " + HOST + ":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()