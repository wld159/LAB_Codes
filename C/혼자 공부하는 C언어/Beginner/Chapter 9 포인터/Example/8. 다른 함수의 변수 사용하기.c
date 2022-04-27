//
// Created by 권경호 on 2021/06/28.
//

#include <stdio.h>

void swap(void);                    // 두 변수 값을 바꾸는 함수 선언

int main(void)
{
    int a = 10, b = 20;             // 변수 선언과 초기화

    swap();                         // 인수 없이 함수 호출
    printf("a : %d, b : %d\n", a, b);               // 변수 a, b 출력

    return 0;
}

void swap(void)                     // 인수가 없으므로 매개변수도 없음
{
    int temp;                                 // 교환을 위한 변수

    temp = a;                                 // temp에 main 함수의 a 값 저장
    a = b;                                    // main 함수의 a에 main 함수의 b 값 저장
    b = temp;                                 // main 함수의 b에 temp 값 저장
}