//
// Created by 권경호 on 2021/06/30.
//

#include <stdio.h>

void add_ten(int a);                            // 함수 선언

int main(void)
{
    int a = 10;

    add_ten(a);                                 // a 값을 복사하여 전달
    printf("a : %d\n", a);

    return 0;
}

void add_ten(a)                                 // 11행의 a와 다른 독립적인 저장 공간 할당
{
    a = a + 10;                                 // 19행의 매개변수 a에 10을 더한다.
}