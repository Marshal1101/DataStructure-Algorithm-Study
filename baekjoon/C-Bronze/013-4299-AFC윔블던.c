#include <stdio.h>

int main()
{
    int sum, diff, a, b;

    scanf("%d%d", &sum, &diff);
    if (sum < diff) {
        printf("-1\n");
        return 0;
    }
    a = (sum + diff);
    if (a % 2 > 0) {
        printf("-1\n");
        return 0;
    }
    b = (sum - diff);
    if (b % 2 > 0) {
        printf("-1\n");
        return 0;
    }
    printf("%d %d\n", a/2, b/2);
    return 0;
}