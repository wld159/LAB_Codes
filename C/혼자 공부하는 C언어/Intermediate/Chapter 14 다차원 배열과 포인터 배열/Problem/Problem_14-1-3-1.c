//
// Created by 권경호 on 2021/07/02.
//

#include <stdio.h>

int main(void)
{
    char mark[5][5] = {0};
    int i, j;

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if (i == j) mark[i][j] = 'X';
            else mark[i][j] = ' ';
            printf("%c", mark[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}