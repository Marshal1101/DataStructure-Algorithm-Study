// https://www.acmicpc.net/source/43842141

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SWAP(T,X,Y){\
    T _temp = X;\
    X = Y;\
    Y = _temp;\
}\
/*SWAP END*/

int calc(char *x, char *y)
{
    for (;*x != '\0' && *y != '\0';x++, y++){
        if(*x == *y)
            continue;
        return (*x < *y) ? -1 : 1;
    }
    return 0;
}

int main(void)
{
    char *x, *y, *a, *b;
    a = (char*)calloc(10003, sizeof(char));
    b = (char*)calloc(10003, sizeof(char));
    
    scanf("%10001[-0-9] %10001[-0-9] ", a, b);
    int sign = 0;
    {
        const int A = (a[0] == '-'), B = (b[0] == '-');
        x = a + (A ? 1 : 0);
        y = b + (B ? 1 : 0);
        sign = (A && !B || !A && B) ? -1 : 1;
    }
    
    int lx = strlen(x) - 1, ly = strlen(y) - 1, c = 0;
    if(lx < ly || lx == ly && sign < 0 && calc(x, y) < 0){
        SWAP(char*, x, y);
        SWAP(char*, a, b);
        SWAP(int, lx, ly);
    }

    for(;ly >= 0; --lx, --ly){
        const int sum = (x[lx] - '0') + sign * (y[ly] - '0') + c;
        x[lx] = '0' + (100 + sum) % 10;
        c = (sum + 100) / 10 - 10;
    }
    if(c != 0){
        for(;lx >= 0;lx--){
            const int sum = (x[lx] - '0') + c;
            x[lx] = '0' + (100 + sum) % 10;
            c = (sum + 100) / 10 - 10;
        }
    }
    
    if(c > 0) {
        if(a[0] == '-') printf("-");
        printf("%d", c);
        printf("%s", x);
    }
    else{
        for(;*x == '0';x++);
        if(*x == '\0')
            printf("0");
        else{
            if(a[0] == '-') printf("-");
            printf("%s", x);
        }
    }
    free(a), free(b);
    return 0;
}