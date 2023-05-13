#include <stdio.h>


int main()
{
    int N, K, i=0, cnt=0, num;
    scanf("%d%d", &N, &K);
    while (i++ < N)
    {
        if (N % i == 0)
        {
            cnt++;
            num = i;
            if (cnt == K)
            {
                printf("%d", num);
                return 0;
            };
        }
    }
    printf("0");
    return 0;
}