//
// Created by 권경호 on 2021/05/18.
//

#include <stdio.h>

int main(void)
{
    int a = 20, b = 10;
    int res;

    res = (++a, ++b);           // 차례로 연산이 수행되며 결과적으로 res에 저장되는 값은 증가된 b의 값이다.
    printf("a : %d, b : %d\n", a, b);
    printf("res : %d\n", res);

    return 0;
}