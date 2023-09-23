#include <stdio.h>
#include <math.h>

int main(void)
{
    int a0, a1, a2, c, n0, disc;
    double x1, x2, tmp;
    scanf("%d%d%d%d%d", &a2, &a1, &a0, &c, &n0);
    
    if (c - a2 < 0) {
        printf("0\n");
    } else if (c - a2 == 0) {
        if (a1 == 0) {
            if (a0 <= 0) {
                printf("1\n");
            } else {
                printf("0\n");
            }
        } else {
            // tmp = 1.0 * a0 / a1;
            // printf("tmp: %lf, n0: %d, tmp-n0: %lf\n", tmp, n0, tmp-n0);
            printf("%d\n", (a1 <= 0 && a1*n0+a0 <= 0) ? 1 : 0);
        }
    } else {
        disc = a1*a1 + 4 * (c - a2) * a0;
        if (disc < 0) {
            printf("1\n");
        } else {
            x1 = (1.0 * a1 - sqrt(disc)) / (2*(c - a2));
            x2 = (1.0 * a1 + sqrt(disc)) / (2*(c - a2));
            // printf("c-a2: %d, disc: %d, sqrt: %lf, x1: %lf, x2: %lf\n", c-a2, disc, sqrt(disc), x1, x2);
            printf("%d\n", (x1 <= n0 && x2 <= n0) ? 1 : 0);
        }
    }
    
    return 0;
}