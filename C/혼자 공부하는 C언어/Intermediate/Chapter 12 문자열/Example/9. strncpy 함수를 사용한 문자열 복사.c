//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>
#include <string.h>                         // strncpy 함수 사용을 위한 헤더 파일 포함

int main(void)
{
    char str[20] = "mango tree";            // 배열 초기화

    strncpy(str, "apple-pie", 5);           // "apple-pie"에서 다섯 문자만 복사

    printf("%s\n", str);                    // 복사 받은 문자열 출력

    return 0;
}