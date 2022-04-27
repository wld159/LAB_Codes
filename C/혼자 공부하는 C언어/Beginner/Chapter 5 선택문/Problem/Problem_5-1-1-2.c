//
// Created by 권경호 on 2021/05/19.
//

#include <stdio.h>

int main(void)
{
    int a;

    printf("a 입력 : ");
    scanf("%d", &a);

    if (a % 2 == 0)
    {
        a = 2;
    }
    else
    {
        a = 1;
    }

    printf("%d", a);

    return 0;
}