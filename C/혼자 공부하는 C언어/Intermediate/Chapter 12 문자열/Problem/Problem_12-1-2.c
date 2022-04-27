//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>

int main(void)
{
    char str[20] = "apple";
    char *pa = str;
    char *pb = "pineapple";

    printf("%s", "apple");
    printf("%s", str[0]);
    printf("%s", pa);
    printf("%s", pb + 4);

    return 0;
}