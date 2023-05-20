#include <stdio.h>

int main()
{
    int i, age, split, cut, ans;

    while (1) {
        scanf("%d", &age);
        if (age == 0) return 0;
        ans = 1;
        for (i = 0; i < age; i++) {
            scanf("%d", &split);
            scanf("%d", &cut);
            ans = ans * split - cut;
        } 
        printf("%d\n", ans);
    }
}