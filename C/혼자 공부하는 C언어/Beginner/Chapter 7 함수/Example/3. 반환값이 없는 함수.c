//
// Created by 권경호 on 2021/06/23.
//

#include <stdio.h>

void print_char(char ch, int count);                // 함수 선언

int main(void)
{
    print_char('@', 5);                     // 문자와 숫자를 주고 함수 호출

    return 0;
}

void print_char(char ch, int count)                 // 매개변수는 있으나 반환형이 없다.
{
    int i;

    for (i = 0; i < count; i++)                     // i는 0부터 count-1까지 증가, count번 증가
    {
        printf("%c", ch);                           // 매개변수 ch에 받은 문자 출력
    }

    return ;
}