#include <stdio.h>


int main()
{
    char name[11];
    int age, wgt;
    while (1) {
        scanf("%s %d %d", name, &age, &wgt);
        if (age == 0 && wgt == 0) break;
        
        if (age > 17 || wgt >= 80) 
        {
            printf("%s Senior\n", name);
        }
        else
        {
            printf("%s Junior\n", name);
        }
    }

    return 0;
}


// main(s,x,y)
// {
//     for(;scanf("%s%d%d",&s,&x,&y),x;puts(x>17|y>79?"Senior":"Junior")) puts(&s);
// }