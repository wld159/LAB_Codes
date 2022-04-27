//
// Created by 권경호 on 2021/07/02.
//

#include <stdio.h>

void input_data(int *pa, int *pb);
void swap_data(void);
void print_data(int a, int b);

int a, b;

int main(void)
{
    input_data(&a, &b);                                     // 전역 변수에 정수 값 입력
    swap_data();                                            // 두 변수 교환
    print_data(a, b);                                       // 교환된 변숫값 출력

    return 0;
}

void input_data(int *pa, int *pb)
{
    printf("두 정수 입력 : ");
    scanf("%d%d", pa, pb);
}

void swap_data(void)
{
    int temp;

    temp = a;
    a = b;
    b = temp;
}

void print_data(int a, int b)
{
    printf("두 정수 출력 : %d, %d\n", a, b);
}