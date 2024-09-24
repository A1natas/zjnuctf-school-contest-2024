from ctypes import * 
import msvcrt
def encrypt(v,k):
	v0=c_uint32(v[0])
	v1=c_uint32(v[1])
	sum1=c_uint32(0)
	delta=0x9e3779b9
	for i in range(32):
		sum1.value+=delta
		v0.value+=((v1.value<<4)+k[0])^(v1.value+sum1.value)^((v1.value>>5)+k[1])
		v1.value+=((v0.value<<4)+k[2])^(v0.value+sum1.value)^((v0.value>>5)+k[3])
	return [v0.value,v1.value]

def any_key_to_exit():
    print("Press any key to exit...")
    while True:
        if msvcrt.kbhit():  # 检测键盘是否有输入
            key = msvcrt.getch()  # 获取输入的键值
            break

if __name__=='__main__':
	enc=[0x89ed6163, 0xed259946,0xd998a419,0x1f206eb3,0x3f3411fe, 0xeba4cfef,
		 0x50dbc70b, 0xbcf80995,0xd40ee125,0xbf37d140,0x6f3a55f5, 0xc0aa5d21,
		 0x34131db5, 0x6c721dcb,0x06ab4cdd,0x96f84b5f,0xb0a5cf98, 0xabbaebbf,
		 0xc3626aa1, 0x630006a6,0x7300d569,0xb8ae5be9,0x212e6a73, 0xcb581d4e,
		 0x6b8a0525, 0xee1d2cc1,0xf079490e,0x2629bfb0,0xfcebaab0, 0x7202e516,
		 0xa37a21f1, 0x05289fd8]
	k=[1,1,4,5]
	print("Welcome to the 4th ZJNU CTF ! please drink my python-tea.")
	flag=input("input your flag:")
	flag1=[ord(char) for char in list(flag)]
	if len(flag1)%2!=0:
		print("wrong!")
	else:
		res=[]
		flag2 = [flag1[i:i+2] for i in range(0, len(flag1), 2)]
		for i in flag2:
			res+=encrypt(i,k)
		if res==enc:
			print("correct!")
		else :
			print("wrong!")
	any_key_to_exit()
