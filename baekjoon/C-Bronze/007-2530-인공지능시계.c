#include <stdio.h>


int main()
{
    int h, m, s, term;
    scanf("%d%d%d", &h, &m, &s);
    scanf("%d", &term);
    h += term / 3600;
    term = term % 3600;
    m += term / 60;
    s += term % 60;
    if (s > 59)
    {
        s %= 60;
        m += 1;
    }
    if (m > 59)
    {
        m %= 60;
        h += 1;
    }
    if (h > 23)
    {
        h %= 24;
    }
    printf("%d %d %d", h, m, s);
}