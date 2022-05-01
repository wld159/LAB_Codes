//
// Created by 권경호 on 2021/07/02.
//

#include <stdio.h>

int main(void)
{
    int num[3][4] = {                       // 2차원 배열의 선언과 초기화
            {1, 2, 3, 4},                   // num의 0행
            {5, 6, 7, 8},                   // num의 1행
            {9, 10, 11, 12}                 // num의 2행
    };
    // int num[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};와 같은 문장임

    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("%5d", num[i][j]);       // 배열 요소 출력
        }
        printf("\n");                       // 한 행을 출력한 후에 줄 바꿈
    }

    return 0;
}