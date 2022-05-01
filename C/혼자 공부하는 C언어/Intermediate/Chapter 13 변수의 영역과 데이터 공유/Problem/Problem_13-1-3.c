//
// Created by 권경호 on 2021/06/30.
//

#include <stdio.h>

int func(void);

int main(void)
{
    int i, sum = 0;

    for (i = 0; i < 10; i++)
    {
        sum += func();
    }

    printf("%d", sum);
    return 0;
}

int func(void)
{
    static int a = 0;
    a++;
    return a;
}