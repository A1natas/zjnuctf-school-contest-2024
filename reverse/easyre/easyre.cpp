#include "base64.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 400000
// base64 转换表, 共64个
static const char alphabet[] = {
	'Z', 'J', 'N', 'U', 'C', 'T', 'F',
	't', 'a', 'b', 'l', 'e', 'M', 'E',
	'O', 'P', 'Q', 'R', 'S', 'G',
	'D', 'V', 'W', 'X', 'Y', 'A',
	'I', 'B', 'c', 'd', 'L', 'f', 'g',
	'h', 'i', 'j', 'k', 'K', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 'H',
	'u', 'v', 'w', 'x', 'y', 'z',
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
	'+', '/'};//ZJNUCTFtableMEOPQRSGDVWXYAIBcdLfghijkKmnopqrsHuvwxyz0123456789+/

static char cmove_bits(unsigned char src, unsigned lnum, unsigned rnum) {
	src <<= lnum; // src = src << lnum;
	src >>= rnum; // src = src >> rnum;
	return src;
}

int encode(const char *indata, int inlen, char *outdata, int *outlen) {
	
	int ret = 0; // return value
	if (indata == NULL || inlen == 0) {
		return ret = -1;
	}
	
	int in_len = 0; // 源字符串长度, 如果in_len不是3的倍数, 那么需要补成3的倍数
	int pad_num = 0; // 需要补齐的字符个数, 这样只有2, 1, 0(0的话不需要拼接, )
	if (inlen % 3 != 0) {
		pad_num = 3 - inlen % 3;
	}
	in_len = inlen + pad_num; // 拼接后的长度, 实际编码需要的长度(3的倍数)
	
	int out_len = in_len * 8 / 6; // 编码后的长度
	
	char *p = outdata; // 定义指针指向传出data的首地址
	
	//编码, 长度为调整后的长度, 3字节一组
	for (int i = 0; i < in_len; i+=3) {
		int value = *indata >> 2; // 将indata第一个字符向右移动2bit(丢弃2bit)
		char c = alphabet[value]; // 对应base64转换表的字符
		*p = c; // 将对应字符(编码后字符)赋值给outdata第一字节
		
		//处理最后一组(最后3字节)的数据
		if (i == inlen + pad_num - 3 && pad_num != 0) {
			if(pad_num == 1) {
				*(p + 1) = alphabet[(int)(cmove_bits(*indata, 6, 2) + cmove_bits(*(indata + 1), 0, 4))];
				*(p + 2) = alphabet[(int)cmove_bits(*(indata + 1), 4, 2)];
				*(p + 3) = '=';
			} else if (pad_num == 2) { // 编码后的数据要补两个 '='
				*(p + 1) = alphabet[(int)cmove_bits(*indata, 6, 2)];
				*(p + 2) = '=';
				*(p + 3) = '=';
			}
		} else { // 处理正常的3字节的数据
			*(p + 1) = alphabet[cmove_bits(*indata, 6, 2) + cmove_bits(*(indata + 1), 0, 4)];
			*(p + 2) = alphabet[cmove_bits(*(indata + 1), 4, 2) + cmove_bits(*(indata + 2), 0, 6)];
			*(p + 3) = alphabet[*(indata + 2) & 0x3f];
		}
		
		p += 4;
		indata += 3;
	}
	
	if(outlen != NULL) {
		*outlen = out_len;
	}
	
	return ret;
}
int Easter()
{
	FILE *inputFile, *outputFile;
	char inputFilename[] = "what_is_me"; // 修改为你的输入文件名
	char outputFilename[] = "mikumiku.jpg"; // 修改为你的输出文件名
	unsigned char buffer[BUFFER_SIZE];
	size_t bytesRead;
	// 打开输入文件
	inputFile = fopen(inputFilename, "rb");
	if (inputFile == NULL) {
		perror("Error opening input file");
		return 0;
	}
	// 读取文件内容到数组
	bytesRead = fread(buffer, sizeof(char), BUFFER_SIZE, inputFile);
	if (bytesRead == 0) {
		perror("Error reading input file");
		fclose(inputFile);
		return 0;
	}
	// 执行异或操作
	for (size_t i = 0; i < bytesRead; i++) {
		buffer[i] ^= 0x24; // 异或运算
	}
	// 创建或打开输出文件
	outputFile = fopen(outputFilename, "wb");
	if (outputFile == NULL) {
		perror("Error opening output file");
		fclose(inputFile);
		return 0;
	}
	// 写入修改后的数据到输出文件
	fwrite(buffer, sizeof(char), bytesRead, outputFile);
	
	// 关闭文件
	fclose(inputFile);
	fclose(outputFile);
	printf("File processed successfully.\n");
	return 0;
}
int main()
{
	char input[100];
	char pw[100]={0x68,0x49,0x54,0x51,0x40,0x73,0x61,0x14,0x65,0x4a,0x6c,0x77,0x65,0x77,0x11,0x5d,0x69,0x62,0x70,0x4f,0x7c,0x5e,0x70,0x5e,0x7c,0x16,0x5c,0x74,0x66,0x49,0x40,0x42,0x7d,0x5e,0x6e,0x6c,0x69,0x17,0x14,0x19};
	printf("Give me your flag,and you will get a gift!:\n");
	int i=0;
	while(scanf("%c", &input[i]) == 1 && input[i] != '\n' &&i<100)
	{
		i++;
	}
	input[i]='\0';
	//printf("%s",input);
	int len=0;
	char str[100] = {};
	encode(input,(int)strlen(input),str,&len);
	for(int p=0;p<len;p++)
	{
		//printf("%c",pw[p]^0x24);
		if((str[p]^0x24)!=pw[p])
		{
			printf("lose!T^T\n");
			break;
		}
		if(p==len-1)
		{
			printf("win!(∠·ω< )~★\n");
			Easter();
		}
	}
	//printf("%s, len=%d\n", str, len);
	//zjnuctf{Re.r0ad_1s_lOng_c0m3}
	return 0;
}
