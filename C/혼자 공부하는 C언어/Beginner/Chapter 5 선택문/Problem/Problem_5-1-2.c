//
// Created by 권경호 on 2021/05/19.
//

#include <stdio.h>

int main(void)
{
    int chest = 95;                 // 가슴둘레의 크기를 저장할 변수
    char size;                      // 옷의 사이즈를 결정해서 저장할 변수

    if (chest <= 90)
    {
        size = 'S';
    }
    else if ((chest > 90) & (chest <= 100))
    {
        size = 'M';
    }
    else
    {
        size = 'L';
    }

    printf("%c", size);

    return 0;
}