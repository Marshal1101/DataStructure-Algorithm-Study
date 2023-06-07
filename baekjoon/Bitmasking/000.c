#include <stdio.h>

void p1() {
    int x=3, y=2;
    float z=2.0;
    printf("%d %d\n", x%y, y%x);
    printf("%d %0.2f\n", x/y, x/z);
}

void p2() {
    int x=11;
    printf("%d", x<<3);
    printf("%d\n", x>>1);
}

void p3() {
    printf("%d", ~12);
}

void p4() {
    int a[3] = {1, 2};
    for (int i=0; i<3; i++) {
        printf("%d ", a[i]);
    }
    char b[4] = {'a', 'b', 'c'};
    for (int i=0; i<4; i++) {
        printf("%c", b[i]);
        printf("%d", b[3]);
        printf("%s", b[3]);
    }
    /* null은 %c로 '', %d로 0, %s로 (null) */
}

void p5() {
    int a[2][3] = {1, 2, 3, 4, };
    int i, j;
    for (i=0; i<2; i++)
        for (j=0; j<3; j++)
            printf("%d ", a[i][j]);
            printf("=");
}

void p6() {
    char a[8] = "Hello!";
    printf("%s\n", a);
    printf("%s\n", a+1);
    printf("%s\n", a+4);
    a[3] = NULL;
    printf("%s\n", a+1);
    printf("%s\n", a+3);
    printf("%s\n", a+4);
}

void p7() {
    char a[2][8] = {"Hello!", "Soojebi"};
    printf("%s\n", a[0]);
    printf("%s\n", a[1]);
    printf("%s\n", a[1]+3);
    a[1][3] = NULL;
    printf("%s\n", a[1]+1);
    printf("%s\n", a[1]+4);
    printf("%s\n", a);
    printf("%s\n", a+1);
    printf("%s\n", *a+1);
    printf("%s\n", &a);
    printf("%s\n", a[1]);
    printf("%s\n", &a[0] + 1);
    printf("%s\n", &a);
}


void p8() {
    char b[3][8] = {"abcde", "fghij", "klm"};
    int a[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    int *r = b;
    printf("sizeof r %d\n", sizeof(r));
    int (*p)[6] = a;
    int (*q)[4] = a+1;
    printf("%d %d %d\n", a[0][0], a[0][1], a[1][0]);
    printf("%s %s %s\n", r, r+1, r+2);
    printf("%c %c %c\n", *r, *(r+1), *(r+4));
    printf("%d %d %d\n", p[0][0], p[0][2], p[1][0]);
    printf("%d %d %d\n", q[0][0], q[1][0], q[2][0]);
}

void p9() {
    int i, input, res=0, bin=1;
    char a[8] = "Hello!";
    printf("%s\n", a);
    scanf("%d", &input);
    while (input != 0) {
        if (input & 1) {
            res += bin;
        }
        bin = bin * 2;
        input /= 10;
    }
    printf("%d", res);
}

void main() {
    p9();
}