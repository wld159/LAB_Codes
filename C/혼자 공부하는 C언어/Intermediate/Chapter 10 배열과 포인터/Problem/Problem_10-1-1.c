//
// Created by 권경호 on 2021/06/28.
//

#include <stdio.h>

int main(void)
{
    double ary[5] = {1.2, 3.5, 7.4, 0.5, 10.0};
    double *pa = ary;
    double *pb = ary + 2;

    printf("%.1lf\n", ary);
    printf("%.1lf\n", *(ary + 1));
    printf("%.1lf\n", pa + 2);
    printf("%.1lf\n", pa[3]);
    printf("%.1lf\n", *pb);
    printf("%.1lf\n", pb - pa);

    return 0;
}