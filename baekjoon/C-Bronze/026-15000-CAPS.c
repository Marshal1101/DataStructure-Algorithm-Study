#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int ch;

    while ((ch = getchar()) + 1) {
        printf("%c", toupper(ch));
    }

    return 0;
}