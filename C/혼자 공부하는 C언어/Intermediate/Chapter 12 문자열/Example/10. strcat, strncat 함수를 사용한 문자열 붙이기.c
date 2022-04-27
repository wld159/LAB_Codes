//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80] = "straw";                     // 문자열 초기화

    strcat(str, "berry");                       // str 배열에 문자열 붙이기
    printf("%s\n", str);
    strncat(str, "piece", 3);                    // str 배열에 3개의 문자 붙이기
    printf("%s\n", str);

    return 0;
}