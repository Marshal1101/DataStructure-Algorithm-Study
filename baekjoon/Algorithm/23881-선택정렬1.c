#include <stdio.h>
#include <stdlib.h>


void selection_sort(int *A, int N, int K)
{
    int i, j, midx, tmp, ex_cnt;
    
    ex_cnt = 0;
    for (i = N-1; i >= 1; i--) {
        midx = i;
        for (j = 0; j <= i; j++) {
            if (A[j] > A[midx]) {
                midx = j;
            }
        }
        if (midx != i) {
            tmp = A[i];
            A[i] = A[midx];
            A[midx] = tmp;
            ex_cnt++;
            if (ex_cnt == K) {
                printf("%d %d\n", A[midx], A[i]);
                return;
            } else if (ex_cnt > K) {
                printf("-1");
                return;
            }
        }
    }

    printf("-1");
}

int main(void)
{
    int i, N, K;
    scanf("%d %d", &N, &K);
    int *A = (int*) malloc(sizeof(int) * N);
    for (i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    selection_sort(A, N, K);

    return 0;
}