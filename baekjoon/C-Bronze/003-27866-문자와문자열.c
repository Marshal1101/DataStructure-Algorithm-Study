#include <string.h>
#include <stdio.h>

int main()
{
    char s1[1001];
    int i;
    scanf("%s", s1);
    scanf("%d", &i);
    printf("%c\n", s1[i-1]);

    return 0;
}