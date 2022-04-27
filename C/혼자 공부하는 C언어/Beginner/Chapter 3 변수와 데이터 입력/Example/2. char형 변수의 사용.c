//
// Created by 권경호 on 2021/05/16.
//

#include <stdio.h>

int main(void)
{
    char ch1 = 'A';     // 문자로 초기화, 저장된 값은 문자의 아스키 코드 값
    char ch2 = 65;      // 문자 'A'의 아스키 코드 갑셍 해당하는 정수로 초기화

    printf("문자 %c의 아스키 코드 값: %d\n", ch1, ch2);
    printf("아스키 코드 값이 %d인 문자 : %c\n", ch1, ch2);

    return 0;
}