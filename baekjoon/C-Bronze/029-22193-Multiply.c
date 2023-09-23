#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX 65536

double PI;

struct complex{
    double r, i;
};

struct complex aa[MAX], bb[MAX], res[MAX];
int ans[140000];
char A[50003], B[50003], C[50003];

struct complex add(struct complex a, struct complex b){
    struct complex res;
    res.r=a.r+b.r;
    res.i=a.i+b.i;
    return res;
}

struct complex subtract(struct complex a, struct complex b){
    struct complex res;
    res.r=a.r-b.r;
    res.i=a.i-b.i;
    return res;
}

struct complex multiply(struct complex a, struct complex b){
    struct complex res;
    res.r=a.r*b.r-a.i*b.i;
    res.i=a.r*b.i+a.i*b.r;
    return res;
}

struct complex divide(struct complex a, struct complex b){
    struct complex res;
    res.r=(a.r*b.r+a.i*b.i)/(b.r*b.r+b.i*b.i);
    res.i=(-a.r*b.i+a.i*b.r)/(b.r*b.r+b.i*b.i);
    return res;
}

void fft(struct complex a[MAX], int n, int inv){
    int i, j, k, bit;
    struct complex w, th, tmp;
    double x;

    for(i=1, j=0; i<n; ++i){
        bit=n>>1;
        while(!((j^=bit) & bit)){
            bit>>=1;
        }
        if(i<j){
            tmp=a[i];
            a[i]=a[j];
            a[j]=tmp;
        }
    }

    for(i=1; i<n; i<<=1){
        x=(inv)?PI/i:-PI/i;
        w.r=cos(x);
        w.i=sin(x);
        for(j=0; j<n; j+=(i<<1)){
            th.r=1;
            th.i=0;
            for(k=0; k<i; ++k){
                tmp=multiply(a[i+j+k], th);
                a[i+j+k]=subtract(a[j+k], tmp);
                a[j+k]=add(a[j+k], tmp);
                th=multiply(th, w);
            }
        }
    }

    if(inv){
        tmp.r=n;
        tmp.i=0;
        for(i=0; i<n; ++i){
            a[i]=divide(a[i], tmp);
        }
    }
}

void big_mul(struct complex res[MAX], struct complex a[MAX], int len_a, struct complex b[MAX], int len_b){
    int i, n=1;

    while(n<len_a+1 || n<len_b+1){
        n<<=1;
    }
    n<<=1;

    // DFT a and b with FFT
    fft(a, n, 0);
    fft(b, n, 0);

    // convolution
    for(i=0; i<n; ++i){
        res[i]=multiply(a[i], b[i]);
    }
    
    // IDFT
    fft(res, n, 1);
    for(i=0; i<n; ++i){
        res[i].r=round(res[i].r);
        res[i].i=round(res[i].i);
    }
}

void str2complex(struct complex comp[MAX], char str[50003], int len, int x){
    int i, j, tmp, flag=(len%x>0);

    for(i=0; i<len/x+flag; ++i){
        tmp=0;
        for(j=x-1; j>=0; --j){
            if(len-(i*x+j)-1<0 || len-(i*x+j)-1>=50003){
                continue;
            }
            if(!str[len-(i*x+j)-1]){
                continue;
            }
            tmp=(tmp*10)+str[len-(i*x+j)-1]-'0';
        }
        comp[i].r=tmp;
    }
}

int main(void){
    int i, j, len_a, len_b, x;
    long long tmp;

	scanf("%s %s", A, B);

    scanf("%s %s", A, B);
    PI=acos(-1);

    len_a=strlen(A);
    len_b=strlen(B);
    if((len_a==1 && A[0]=='0') || (len_b==1 && B[0]=='0')){
        printf("0");
        return 0;
    }

    x=3;
    str2complex(aa, A, len_a, x);
    str2complex(bb, B, len_b, x);

    big_mul(res, aa, len_a/x+(len_a%x>0), bb, len_b/x+(len_b%x>0));

    for(i=0; i<MAX; ++i){
        tmp=(long long)res[i].r;
        j=0;
        while(tmp && i*x+j<140000){
            ans[i*x+j]+=(int)(tmp%10LL);
            tmp/=10LL;
            ++j;
        }
    }
    for(i=0; i<139999; ++i){
        if(ans[i]>=10){
            ans[i+1]+=ans[i]/10;
            ans[i]%=10;
        }
    }

    x=0;
    if(ans[len_a+len_b-1]!=0){
        C[x++]=ans[len_a+len_b-1]+'0';
    }
    for(i=len_a+len_b-2; i>=0; --i){
        C[x++]=ans[i]+'0';
    }
    C[x]=0;
    printf("%s", C);

    return 0;
}