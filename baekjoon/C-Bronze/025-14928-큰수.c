#include <stdio.h>


int mod(char *S, int p);


int main(void)
{
    char S[1000003];

    scanf("%s", S);
    printf("%d\n", mod(S, 20000303));
    return 0;
}

int mod(char *S, int p)
{
	// S는 수를 문자열로 표현한 것, 1324 -> "1324"
	int ret = 0;
	for (int i = 0; S[i]; i++) ret = (ret*10 + (S[i]-'0')) % p;
	return ret;
}