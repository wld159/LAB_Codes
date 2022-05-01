//
// Created by 권경호 on 2021/06/30.
//

#include <stdio.h>

void func(void);

int a = 10;

int main(void)
{
    a = 20;
    func();
    printf("%d", a);
    return 0;
}

void func(void)
{
    a = 30;
}