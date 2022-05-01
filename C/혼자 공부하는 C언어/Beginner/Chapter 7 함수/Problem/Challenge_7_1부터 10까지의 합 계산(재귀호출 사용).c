//
// Created by 권경호 on 2021/06/30.
//

#include <stdio.h>

int rec_func(int n);                                // 1부터 n까지의 합을 반환하는 함수

int main(void)
{
    int res;

    res = rec_func(10);
    printf("result : %d\n", res);

    return 0;
}

int rec_func(int n)
{
    if (n == 1) return 1;
    else return (n + rec_func(n - 1));
}