#ifndef base64_h
#define base64_h

#include <stdio.h>

#if __cplusplus
extern "C"{
#endif
	
	int encode(const char *indata, int inlen, char *outdata, int *outlen);
	
#if __cplusplus
}
#endif

#endif /* base64_h */
