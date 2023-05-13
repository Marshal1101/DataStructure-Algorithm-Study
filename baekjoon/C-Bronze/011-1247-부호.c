#include <stdio.h>
/* 128비트 사용 풀이 */
main(n) {
	for (int i = 0; i < 3; i++) {
		__int128_t t = 0;
		scanf("%d", &n);
		while (n--) {
			scanf("%ld", &x);
			t += x;
		}
		puts(t ? t > 0 ? "+" : "-" : "0");
	}
}



/* 오버플로우 관리 풀이 */
#include <limits.h>


int main(void) {

    int N;
    char sign[4];
    long long sum = 0;
    long long num = 0;

    for (int i = 0; i < 3; i++)
    {
        int overflow = 0;
        sum = 0;
        scanf("%d", &N);
        for (int j = 0; j < N; j++)
        {
            scanf("%lld", &num);

            if (sum > 0 && num > 0 && sum > (LLONG_MAX-num))
            {
                overflow++;
                sum += num;
            }
            else if (sum < 0 && num < 0 && sum < (LLONG_MIN-num))
            {
                overflow--;
                sum += num;
            }
            else
                sum += num;
        }

        if (overflow == 0)
        {
            if (sum > 0)
                sign[i] = '+';
            else if (sum < 0)
                sign[i] = '-';
            else
                sign[i] = '0';
        }
        else if (overflow > 0)
            sign[i] = '+';
        else
            sign[i] = '-';
    }
    sign[3] = 0;

    printf("%c\n", sign[0]);
    printf("%c\n", sign[1]);
    printf("%c\n", sign[2]);

    return 0;
}