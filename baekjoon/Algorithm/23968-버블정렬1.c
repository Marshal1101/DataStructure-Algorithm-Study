#include <stdio.h>
#include <stdlib.h>


void bubble_sort(int *A, int N, int K)
{
    int i, j, tmp, cnt;

    cnt = 0;
    for (i = N-1; i > 0; i--) {
        for (j = 0; j < i; j++) {
            if (A[j] > A[j+1]) {
                tmp = A[j];
                A[j] = A[j+1];
                A[j+1] = tmp;
                cnt++;
                if (cnt == K) {
                    printf("%d %d", A[j], A[j+1]);
                    return;
                } else if (cnt > K) {
                    printf("-1");
                    return;
                }
            }
        }
    }

    printf("-1");
}


int main(void)
{
    int i, N, K;
    scanf("%d %d", &N, &K);
    int *A = (int *) malloc(sizeof(int) * N);
    for (i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    bubble_sort(A, N, K);
    return 0;
}