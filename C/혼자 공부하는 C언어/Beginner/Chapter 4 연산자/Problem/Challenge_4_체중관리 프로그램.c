//
// Created by 권경호 on 2021/05/19.
//

#include <stdio.h>

int main(void)
{
    double weight, height, BMI;

    printf("몸무게(kg)와 키(cm) 입력 : ");
    scanf("%lf%lf", &weight, &height);

    height = height * 0.01;
    BMI = weight / (height * height);
    printf((BMI >= 20.0) & (BMI < 25.0) ? "표준입니다." : "체중 관리가 필요합니다.");

    return 0;
}