//
// Created by 권경호 on 2021/06/28.
//

#include <stdio.h>

int main(void)
{
    double ary[5] = {1.2, 3.5, 7.4, 0.5, 10.0};
    double *pa = ary;
    double *pb = ary + 2;
    int i;

    for (i = 0; i < 3; i++)
    {
        printf("%.1lf\n", *pb);
        *pb++;
    }
}