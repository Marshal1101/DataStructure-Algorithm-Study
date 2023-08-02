#include <stdio.h>


int main(void)
{
    long long int i, t, lt, wt, le, we;

    scanf("%I64d", &t);
    for (i = 0; i < t; i++) {
        scanf("%I64d %I64d %I64d %I64d", &lt, &wt, &le, &we);
        printf("%s\n", (lt * wt > le * we ? "TelecomParisTech" : (lt * wt < le * we ? "Eurecom" : "Tie")));
    }
    return 0;
}