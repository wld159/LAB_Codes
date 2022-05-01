//
// Created by 권경호 on 2021/06/30.
//

#include <stdio.h>

int main(void)
{
    register int i;                             // 레지스터 변수
    auto int sum = 0;                           // auto 지역 변수

    for (i = 1; i <= 10000; i++)                // 반복 과정에서 i를 계속 사용함
    {
        sum += i;
    }

    printf("%d\n", sum);

    return 0;
}