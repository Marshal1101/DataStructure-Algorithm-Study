#include <stdio.h>

int main()
{
    int n, k, ans;

    while (1) {
        scanf("%d", &n);
        if (n == 0) break;
        ans = 1;
        while (n > 0) {
            k = n % 10;
            n /= 10;
            ans += 1;
            switch (k)
            {
            case 0:
                ans += 4;
                break;
            case 1:
                ans += 2;
                break;
            default:
                ans += 3;
                break;
            }
        }
        printf("%d\n", ans);
    }
}