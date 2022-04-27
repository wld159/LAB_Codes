//
// Created by 권경호 on 2021/05/19.
//

#include <stdio.h>

int main(void)
{
    int a;

    printf("a 입력 : ");
    scanf("%d", &a);

    if (a < 0)
    {
        a = -a;
    }

    printf("%d", a);

    return 0;
}