#include <stdio.h>

int main()
{
    int n1, n2, n1r, n1c, n2r, n2c, ans;

    ans = 0;
    scanf("%d%d", &n1, &n2);
    n1r = (n1 - 1) % 4;
    n2r = (n2 - 1) % 4;
    n1c = (n1 - 1) / 4;
    n2c = (n2 - 1) / 4;
    ans += (n1r > n2r ? n1r - n2r : n2r - n1r);
    ans += (n1c > n2c ? n1c - n2c : n2c - n1c); 
    printf("%d\n", ans);
    return 0;
}