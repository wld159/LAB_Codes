//
// Created by 권경호 on 2021/06/23.
//

#include <stdio.h>

double centi_to_meter(int x);             // 함수 선언

int main(void)
{
    double res;                                     // 함수의 반환값을 저장할 변수

    res = centi_to_meter(187);                      // 함수 호출, 반환값을 res에 저장
    printf("%.2lfm\n", res);                          // 반환된 res의 값 출력

    return 0;
}

double centi_to_meter(int x)              // 함수 정의 시작
{
    double temp;                                     // 필요한 변수 선언
    temp = x * 0.01;                                 // 매개변수 cm의 값을 m단위로 환산
    return temp;                                     // 환산된 값 반환
}