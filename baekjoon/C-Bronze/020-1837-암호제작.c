#include <stdio.h>
#include <math.h>

int mod(char * S, int p);
int IsPrimeNumber(int num);

int main()
{
    char P[103];
    int i, K;

    scanf("%s%d", P, &K);
    for (i = 2; i < K; i++) {
        if (IsPrimeNumber(i) && mod(P, i) == 0) {
            printf("BAD %d\n", i);
            return 0;
        }
    }
    printf("GOOD\n");
    return 0;
}

int mod(char *S, int p)
{
	// S는 수를 문자열로 표현한 것, 1324 -> "1324"
	int ret = 0;
	for (int i = 0; S[i]; i++) ret = (ret*10 + (S[i]-'0')) % p;
	return ret;
}

int IsPrimeNumber(int num)
{
    int i, limit;
    if (num < 2) return 0;
    if (num == 2) return 1;
    limit = sqrt(num) + 1;
    for (i = 3; i <= limit; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}