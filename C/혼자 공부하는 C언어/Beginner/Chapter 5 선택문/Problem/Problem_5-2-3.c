//
// Created by 권경호 on 2021/05/20.
//

#include <stdio.h>

int main(void)
{
    int age = 25, chest = 95;
    char size;

    if (age < 20)                   // 나이가 20 미만이면
    {
        if (chest < 85)             // 20세 미만 chest 값에 따라 사이즈를 결정
            size = 'S';
        else if ((chest >= 85) & (chest < 95))
            size = 'M';
        else
            size = 'L';
    }
    else                            // 나이가 20보다 크거나 같으면
    {
        if (chest < 90)             // 20세 이상 chest 값에 따라 사이즈를 결정
            size = 'S';
        else if ((chest >= 90) & (chest < 100))
            size = 'M';
        else
            size = 'L';
    }
    printf("사이즈는 %c입니다.", size);

    return 0;
}