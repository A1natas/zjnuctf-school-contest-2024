#include<stdio.h>
int main(){
	int n=32;//pw的个数
	unsigned int pw[32]={
		0x89ed6163, 0xed259946,0xd998a419,0x1f206eb3,0x3f3411fe, 0xeba4cfef,
		0x50dbc70b, 0xbcf80995,0xd40ee125,0xbf37d140,0x6f3a55f5, 0xc0aa5d21,
		0x34131db5, 0x6c721dcb,0x06ab4cdd,0x96f84b5f,0xb0a5cf98, 0xabbaebbf,
		0xc3626aa1, 0x630006a6,0x7300d569,0xb8ae5be9,0x212e6a73, 0xcb581d4e,
		0x6b8a0525, 0xee1d2cc1,0xf079490e,0x2629bfb0,0xfcebaab0, 0x7202e516,
		0xa37a21f1, 0x05289fd8};//可改
	unsigned int v0;
	unsigned int v1;
	unsigned int sum;
	unsigned int key[4]={1,1,4,5};//可改
	for(int i=0;i<n/2;i++)
	{
		v0=pw[2*i];
		v1=pw[2*i+1];
		sum=-32*0x61C88647;
		for(int i=0;i<32;i++)
		{
			v1 -= ((v0 >> 5) + key[3] )^ (16 * v0 + key[2]) ^ (sum + v0);//容易魔改	
			v0 -= ((v1 >> 5) + key[1]) ^ (16 * v1 + key[0]) ^ (sum + v1);
			sum += 0x61C88647;//容易魔改
		}
		for (int j = 0; j<=3; j++)
		{
			printf("%c", (v0 >> (j * 8)) & 0xFF);
		}
		for (int j = 0; j<=3; j++)
		{
			printf("%c", (v1 >> (j * 8)) & 0xFF);
		}
	}
}

//zjnuctf{1et_us_dr1nk_pyth0n_t3a}
