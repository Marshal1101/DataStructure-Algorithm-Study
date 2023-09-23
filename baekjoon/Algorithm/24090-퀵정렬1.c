#include <stdio.h>
#include <stdlib.h>

static int N, K;
static int excnt = 0;

int partition(int A[], int p, int r)
{
    int i, j, pivot, temp;

    pivot = A[r];
    i = p - 1;
    for (j = p; j < r; j++) {
        if (A[j] <= pivot) {
            temp = A[++i];
            A[i] = A[j];
            A[j] = temp;
            excnt++;
            // printf("excnt1: %d, %d<=>%d, i:%d, j:%d => ", excnt, A[i], A[j], i, j);
            // for (int k = 0; k < N; k++) {
            //     printf("%d ", A[k]);
            // }
            // printf("\n");
            if (excnt == K) {
                printf("%d %d\n", A[i], A[j]);
                return -1;
            }
        }
    }
    if (i + 1 != r) {
        temp = A[i+1];
        A[i+1] = A[r];
        A[r] = temp;
        excnt++;
        // printf("excnt2: %d, %d<=>%d, i+1:%d, r:%d => ", excnt, A[i+1], A[r], i+1, r);
        // for (int k = 0; k < N; k++) {
        //     printf("%d ", A[k]);
        // }
        // printf("\n");
        if (excnt == K) {
            printf("%d %d\n", A[i+1], A[r]);
            return -1;
        }
    }

    return (i + 1);
}

void quick_sort(int A[], int p, int r)
{
    int q;

    if (p < r) {
        q = partition(A, p, r);
        if (q == -1) {
            return;
        }
        quick_sort(A, p, q - 1);
        quick_sort(A, q + 1, r);
    }
}

int main(void)
{
    int i;

    scanf("%d %d", &N, &K);
    int *A = (int *) malloc(sizeof(int) * N);
    for (i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    quick_sort(A, 0, N-1);

    if (excnt < K) {
        printf("-1");
    }

    return 0;
}