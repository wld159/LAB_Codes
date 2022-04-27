//
// Created by 권경호 on 2021/06/28.
//

#include <stdio.h>

void print_ary(int *pa, int size);                      // 함수 선언, 매개변수 2개

int main(void)
{
    int ary1[5] = {10, 20, 30, 40, 50};                 // 배열 요소가 5개인 배열
    int ary2[7] = {10, 20, 30, 40, 50, 60, 70};         // 요소의 개수가 7개인 배열

    print_ary(ary1, 5);                             // ary1 배열 출력, 배열 요소의 개수 전달
    printf("\n");
    print_ary(ary2, 7);                             // ary2 배열 출력, 배열 요소의 개수 전달

    return 0;
}

void print_ary(int *pa, int size)                       // 배열명과 배열 요소의 개수를 받는 매개변수 선언
{
    int i;

    for (i = 0; i < size; i++)                          // size의 값에 따라 반복 횟수 결정
    {
        printf("%d ", pa[i]);
    }
}