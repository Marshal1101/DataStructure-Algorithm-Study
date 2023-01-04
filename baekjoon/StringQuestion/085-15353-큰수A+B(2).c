#include <stdio.h>
#include <string.h>

int main() {
    int n1, n2, len1, len2, idx=0, carry=0, ans[10001];
    char str1[10001], str2[10001];

    scanf("%s%s", str1, str2);
    len1 = strlen(str1);
    len2 = strlen(str2);
    while (len1 || len2 || carry) {
        if (len1) n1 = str1[(len1--) - 1] - '0';
        if (len2) n2 = str2[(len2--) - 1] - '0';
        ans[idx++] = (n1 + n2 + carry) % 10;
        carry = n1 + n2 + carry > 9 ? 1 : 0;
        n1 = n2 = 0; 
    }
    for (int i = idx-1; i >= 0; i--) printf("%d", ans[i]);
    return 0;
}