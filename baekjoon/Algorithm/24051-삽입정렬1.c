#include <stdio.h>
#include <stdlib.h>


void insertion_sort(int *A, int N, int K)
{
    int i, loc, newItem, cnt;

    cnt = 0;
    for (i = 1; i < N; i++) {
        loc = i - 1;
        newItem = A[i];

        // 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
        while (0 <= loc && newItem < A[loc]) {
            A[loc+1] = A[loc];
            cnt++;
            if (cnt == K) {
                printf("%d\n", A[loc+1]);
                return;
            } else if (cnt > K) {
                printf("-1\n");
                return;
            }
            loc--;
        }

        // 자리에 newItem 배치
        if (loc + 1 != i) {
            A[loc+1] = newItem;
            cnt++;
            if (cnt == K) {
                printf("%d\n", A[loc+1]);
                return;
            }
        }
    }

    printf("-1\n");
}

int main(void)
{
    int i, N, K;
    scanf("%d %d", &N, &K);
    int *A = (int *) malloc(sizeof(int) * N);
    for (i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    insertion_sort(A, N, K);

    return 0;
}