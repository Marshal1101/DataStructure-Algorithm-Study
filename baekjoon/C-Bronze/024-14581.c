#include <stdio.h>

int main(void)
{
    char id[21];
    char *fan = "fan";
    
    scanf("%s", id);
    printf(":%s::%s::%s:\n", fan, fan, fan);
    printf(":%s::%s::%s:\n", fan, id, fan);
    printf(":%s::%s::%s:\n", fan, fan, fan);
    
    return 0;
}