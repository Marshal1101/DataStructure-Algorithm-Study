#include <stdio.h>


// int main()
// {
//     int l, p, sum, a, b, c, d, e;
//     scanf("%d %d", &l, &p);
//     scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
//     sum = l * p;
//     a = a - sum;
//     b = b - sum;
//     c = c - sum;
//     d = d - sum;
//     e = e - sum;
//     printf("%d %d %d %d %d", a, b, c, d, e);
//     return 0;
// }


n, m;
main(t)
{
    scanf("%d%d",&n,&m);
    while(scanf("%d",&t)+1)printf("%d ",t-n*m);
}