//
// Created by 권경호 on 2021/07/04.
//

#include <stdio.h>

int main(void)
{
    int ary[5] = {10, 20, 30, 40, 50};
    void *vp = ary;

    printf("%d", *((int *)vp + 2));

    return 0;
}