//
// Created by 권경호 on 2021/06/23.
//

#include <stdio.h>

int main(void)
{
    int i, j;

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if ((i + j == 4) || (i == j))
                printf("*");
            else
                printf(" ");
            }
        printf("\n");
        }
    return 0;
}