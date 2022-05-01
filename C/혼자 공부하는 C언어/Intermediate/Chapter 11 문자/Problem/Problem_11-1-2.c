//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>

int main(void)
{
    char ch;

    printf("문자 입력 : ");
    ch = getchar();                                             // 문자 입력
    printf("%c문자의 아스키 코드 값 : %d", ch, ch);                  // %d로 아스키 코드 값 출력
    return 0;
}