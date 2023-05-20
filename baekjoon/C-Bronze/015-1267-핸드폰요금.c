#include <stdio.h>

int main()
{
    int i, n, yCost, mCost;
    int arr[10001];

    scanf("%d", &n);
    for (i = 0; i < n; i++) scanf("%d", &arr[i]);
    yCost = mCost = 0;
    for (i = 0; i < n; i++) {
        yCost += (arr[i] / 30 + (arr[i] % 29 > 0)) * 10;
        mCost += (arr[i] / 60 + (arr[i] % 59 > 0)) * 15;
    }
    if (yCost < mCost) {
        printf("Y %d", yCost);
    } else if (yCost > mCost) {
        printf("M %d", mCost);
    } else {
        printf("Y M %d", yCost);
    }
    return 0;
}