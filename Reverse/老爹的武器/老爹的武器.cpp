#include <Windows.h>
#include <stdio.h>
#include "blowfish_head.h"
#define unsigned char byte

ULONG SearchTable(ULONG leftPart)
{
	ULONG value;
	//查表操作 每一个字节查一次表 然后进行加和异或操作
	value = s_box[0][leftPart >> 24] + s_box[1][(leftPart >> 16) & 0xff];
	value ^= s_box[2][(leftPart >> 8) & 0xff];
	value += s_box[3][leftPart & 0xff];
	return value;
}
//BlowFish的主加密函数 它对明文的加密和对密钥的变换都是利用这个 迭代变换16轮
inline void BF_Fn(ULONG &leftPart, ULONG &rightPart)
{
	int i;
	
	for (i = 0; i < 16; i += 2) {
		leftPart ^= p_box[i];
		rightPart ^= SearchTable(leftPart);
		rightPart ^= p_box[i + 1];
		leftPart ^= SearchTable(rightPart);
	}
	
	leftPart ^= p_box[16];
	rightPart ^= p_box[17];
	
	//最后交换一下
	ULONG temp = leftPart;
	leftPart = rightPart;
	rightPart = temp;
	
}

//对pBox和sBox进行变换
void ExchangeBox(byte *key)
{
	int i, j;
	int keyLen = strlen((const char *)key);//获取key长度
	ULONG *keyLong = NULL;
	ULONG leftPart = 0, rightPart = 0;//得到共计64bit的左右两部分
	keyLong = (ULONG *)malloc(keyLen * sizeof(byte));//获取应得的空间
	ZeroMemory(keyLong, keyLen * sizeof(byte));
	keyLen = keyLen / sizeof(ULONG);
	
	for (i = 0; i < keyLen ; i++) {
		keyLong[i] = _byteswap_ulong(*((ULONG *)key + i));
	}
	
	for (i = 0; i < 18; i++) {//进行异或
		p_box[i] ^= keyLong[i % keyLen];
	}
	
	leftPart = rightPart = 0;//产生一个64位全0数据
	for (i = 0; i < 18; i += 2) {//变换pBox
		BF_Fn(leftPart, rightPart);
		p_box[i] = leftPart;
		p_box[i + 1] = rightPart;
	}
	
	for (i = 0; i < 4; i++) {//变换sBox
		for (j = 0; j < 256; j += 2) {//256 / 2 == 128
			BF_Fn(leftPart, rightPart);
			s_box[i][j] = leftPart;
			s_box[i][j + 1] = rightPart;
		}
	}
}
//p_box s_box
void encrypt(byte *key, byte *data)
{
	int i;
	int dataLen = strlen((const char *)data) / (sizeof(ULONG) * 2);//获取data长度
	byte *dataCopy = data;//建立一个data副本 方便进行指针偏移
	ULONG leftPart, rightPart;
	ExchangeBox(key);
	
	//至此就可以加密明文了 一次加密2 * 4字节大小
	for (i = 0; i < dataLen; i++) {
		leftPart = _byteswap_ulong(*((ULONG *)dataCopy));
		rightPart = _byteswap_ulong(*((ULONG *)dataCopy + 1));
		BF_Fn(leftPart,rightPart);
		*((ULONG *)dataCopy) = _byteswap_ulong(leftPart);
		*((ULONG *)dataCopy + 1) = _byteswap_ulong(rightPart);
		dataCopy += sizeof(ULONG) * 2;//指向下一个数据块
	}	
}
int main()
{
	printf("Welcome to the 4th zjnuctf competition!\n");
	printf("please give your flag(16 bit):");
	byte flag[20]; 
	byte test[20]={0x9d,0xe,0xc0,0x4b,0xa4,0x4e,0x1,0xaa,0x19,0xea,0xa0,0x30,0x2a,0x66,0xa9,0xf};
	byte key[]="hetuno.O";
	for(int i=0;i<16;i++)
	{
		scanf("%c",&flag[i]);
	}
	encrypt(key,flag);//zjnuctf{pAn9ba1}
	for(int i=0;i<16;i++)
	{
		if(flag[i]!=test[i])
		{
			printf("Oh,no!You are wrong!");
			break;
		}
		if(i==15)
		{
			printf("Congratulations to you!");
		}
	}
	system("pause");
	return 0;
}

