//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>

int main(void)
{
    char small, cap ='G';                       // char형 변수 선언과 초기화

    if ((cap >= 'A') && (cap <= 'Z'))           // 대문자 범위라면
    {
        small = cap + ('a' - 'A');              // 대/소문자 차이를 더해 소문자로 변
    }
    printf("대문자 : %c %c", cap, '\n');           // '\n'를 %c로 출력하면 줄이 바뀐다.
    printf("소문자 : %c", small);

    return 0;
}