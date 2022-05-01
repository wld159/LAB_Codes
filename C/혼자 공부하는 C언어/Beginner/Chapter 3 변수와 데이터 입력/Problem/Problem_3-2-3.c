//
// Created by 권경호 on 2021/05/16.
//

#include <stdio.h>

int main(void)
{
    char ch;                // 문자를 저장할 변수

    printf("문자 입력 : ");     // 입력 안내 메시지
    scanf("%c", &ch);            // 변수 ch에 문자 입력
    printf("%c의 아스키 코드 값은 %d입니다.", ch, ch);     // 변환해서 출력

    return 0;
}