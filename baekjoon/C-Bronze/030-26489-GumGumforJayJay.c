#include <stdio.h>

int main(void)
{
    int cnt;
    char c;
    
    while ((c=getchar()) != EOF) {
        if (c =='\n') cnt++;
    }
    printf("%d\n", cnt);
    return 0;
}