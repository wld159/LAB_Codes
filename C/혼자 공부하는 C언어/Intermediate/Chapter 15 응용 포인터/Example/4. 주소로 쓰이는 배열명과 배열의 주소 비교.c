//
// Created by 권경호 on 2021/07/03.
//

#include <stdio.h>

int main(void)
{
    int ary[5];

    printf(" ary의 값 : %u\t", ary);                      // 주소로서의 배열명의 값
    printf("ary의 주소 : %u\n", &ary);                     // 배열의 주소
    printf(" ary + 1 : %u\t", ary + 1);
    printf("&ary + 1 : %u\n", &ary + 1);

    return 0;
}