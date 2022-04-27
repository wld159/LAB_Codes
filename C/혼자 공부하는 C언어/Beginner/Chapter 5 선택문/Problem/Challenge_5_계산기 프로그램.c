//
// Created by 권경호 on 2021/05/20.
//

#include <stdio.h>

int main(void)
{
    int a, b, res;
    char c;

    printf("사칙연산 입력(정수) : ");
    scanf("%d%c%d", &a, &c, &b);

    if (c == '+')
    {
        res = a + b;
        printf("%d%c%d=%d", a, c, b, res);
    }
    else if (c == '-')
    {
        res = a - b;
        printf("%d%c%d=%d", a, c, b, res);
    }
    else if (c == '*')
    {
        res = a * b;
        printf("%d%c%d=%d", a, c, b, res);
    }
    else
    {
        res = a / b;
        printf("%d%c%d=%d", a, c, b, res);
    }

    return 0;
}