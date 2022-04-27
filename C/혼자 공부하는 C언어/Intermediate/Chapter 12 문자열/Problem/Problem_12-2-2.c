//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];
    strcpy(str, "wine");
    strcat(str, "apple");
    strncpy(str, "pear", 1);
    printf("%s, %d\n", str, strlen(str));
    return 0;
}