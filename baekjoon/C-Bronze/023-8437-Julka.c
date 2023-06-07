#include <stdio.h>
#include <string.h>

typedef struct bigint {
    int num[128];
    int len;
} bigint_s;

void print_big(bigint_s *x)
{
    int i, j = x->len - 1;
    
    while(x->num[j] == 0) j--;
    
    for(int i = j; i > -1; i--)
        printf("%d", x->num[i]);
    printf("\n");
}

void copy_big(bigint_s *dest, bigint_s *src)
{
    memcpy(dest->num, src->num, sizeof(int) * src->len);
    dest->len = src->len;
}

void subtract_big(bigint_s *x, bigint_s *y, bigint_s *result)
{
    int i, j;
    
    copy_big(result, x);
    
    for(i = 0; i < y->len; i++)
    {
        result->num[i] -= y->num[i];
        j = i;
        while(result->num[j] < 0)
        {
            result->num[j] += 10;
            result->num[j + 1] -= 1;
            j++;
        }
    }
}

void divide_by_2_big(bigint_s *x, bigint_s *result)
{
    int i, j;
    
    copy_big(result, x);
    
    for(i = result->len - 1; i > -1; i--)
    {
        if(result->num[i] % 2)
        {
            result->num[i] -= 1;
            result->num[i - 1] += 10;
        }
        result->num[i] /= 2;
    }
}

int main()
{
    char buffer[128];
    bigint_s total, diff;
    bigint_s k, n, tmp;
    int i;
    
    scanf("%s", buffer);
    total.len = strlen(buffer);
    for(i = 1; i <= total.len; i++)
        total.num[total.len - i] = buffer[i - 1] - '0';
    
    scanf("%s", buffer);
    diff.len = strlen(buffer);
    for(i = 1; i <= diff.len; i++)
        diff.num[diff.len - i] = buffer[i - 1] - '0';
    
    subtract_big(&total, &diff, &tmp);
    divide_by_2_big(&tmp, &n);
    subtract_big(&total, &n, &k);
    
    print_big(&k);
    print_big(&n);
    
    return 0;
}
