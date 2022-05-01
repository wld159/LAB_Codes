//
// Created by 권경호 on 2021/06/27.
//

#include <stdio.h>

int main(void)
{
    int a = 10;
    int *p = &a;
    *p = 20;
    printf("%d", a);
}