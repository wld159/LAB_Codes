//
// Created by 권경호 on 2021/06/22.
//

#include <stdio.h>

int main(void)
{
    int a = 1;              // 변수를 선언하고 1로 초기화

    do
    {
        a = a * 2;          // a의 값을 2배로 늘린다.
    } while (a < 10);       // a가 10보다 작으면 13행을 반복
    printf("a : %d\n", a);  // 반복이 끝난 후 a 값 출력

    return 0;
}