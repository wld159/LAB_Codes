//
// Created by 권경호 on 2021/05/16.
//

#include <stdio.h>

int main(void)
{
    int age;                // 나이는 정수형
    double height;          // 키는 실수형

    printf("나이와 키를 입력하세요 : ");      // 입력 안내 메시지 출력
    scanf("%d%lf", &age, &height);      // 나이와 키를 입력
    printf("나이는 %d살, 키는 %.1lfcm입니다.", age, height);     // 입력값 출력

    return 0;
}