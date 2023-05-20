#include <stdio.h>

int main()
{
    int i, N, c, ans;

    scanf("%d", &N);
    scanf("%d", &ans);
    for (i = 1; i < N; i++) {
        scanf("%d", &c);
        ans += c - 1;
    }
    printf("%d", ans);
    return 0;
}