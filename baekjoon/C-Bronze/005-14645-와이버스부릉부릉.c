#include <stdio.h>


int main()
{
    int N, K, i, j;
    scanf("%d %d", &N, &K);
    int arr[N][K];
    for (i=0; i<N; i++) 
    {
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }

    printf("비와이");
    return 0;
}