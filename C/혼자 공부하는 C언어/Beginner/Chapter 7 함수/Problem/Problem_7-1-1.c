//
// Created by 권경호 on 2021/06/23.
//

#include <stdio.h>

double average(double a, double b);

int main(void)
{
    double res;                           // 반환값을 저장할 변수 선언
    res = average(1.5, 3.4);        // 함수 호출
    printf("average: %.2lf\n", res);
}

double average(double a, double b)                    // 함수 정의
{
    double temp;
    temp = a + b;
    return (temp / 2.0);
}