//
// Created by 권경호 on 2021/05/19.
//

#include <stdio.h>

int main(void)
{
    int a = 10;

    if (a >= 10)
    {
        a = 1;                  // a가 0보다 크거나 같으면 a에 1 대입
    }
    else
    {
        a =  -1;                // a가 0보다 작으면 a에 -1 대입
    }

    printf("a : %d\n", a);

    return 0;
}