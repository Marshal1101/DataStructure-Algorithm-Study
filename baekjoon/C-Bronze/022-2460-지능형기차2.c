#include <stdio.h>


int main()
{
    int curr, in, out, ans;
    
    ans = curr = 0;
    while (scanf("%d%d", &out, &in) != EOF) {
        curr -= out;
        curr += in;
        if (curr > ans) ans = curr;
    }
    printf("%d\n", ans);
    return 0;
}