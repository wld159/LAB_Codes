//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];
    char str_omit[80];
    char *star = "***********";

    printf("단어 입력 : ");
    scanf("%s", str);

    if (strlen(str) <= 5)
    {
        strcpy(str_omit, str);
    }
    else
    {
        strncpy(str_omit, str, 5);
        str_omit[5] = '\0';
        strncat(str_omit, star, strlen(str) - 5);
    }
    printf("입력한 단어 : %s, 생략한 단어 : %s\n", str, str_omit);

    return 0;
}