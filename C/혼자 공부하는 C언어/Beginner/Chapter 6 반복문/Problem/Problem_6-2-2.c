//
// Created by 권경호 on 2021/06/22.
//

#include <stdio.h>

int main(void)
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("Be Happy~\n");
            if (j == 2) break;
        }
    }
}