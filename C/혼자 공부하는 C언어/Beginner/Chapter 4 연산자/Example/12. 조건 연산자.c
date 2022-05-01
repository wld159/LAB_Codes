//
// Created by 권경호 on 2021/05/18.
//

#include <stdio.h>

int main(void)
{
    int a = 10, b = 20, res;

    res = (a > b) ? a : b;                  // a와 b 중에 큰 값이 res에 저장
    printf("큰 값: %d\n", res);

    return 0;
}