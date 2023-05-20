#include <stdio.h>

int main()
{
    int i, m, from, to, bp;
    scanf("%d", &m);
    bp = 1;
    for (i = 0; i < m; i++) {
        scanf("%d%d", &from, &to);
        if (bp == from) {
            bp = to;
        }
        else if (bp == to) {
            bp = from;
        }
    }
    printf("%d\n", bp);
    return 0;
}