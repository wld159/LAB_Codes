//
// Created by 권경호 on 2021/06/30.
//

#include <stdio.h>

int main(void)
{
    char str[80];
    int i;
    int cnt;

    printf("문장 입력 : ");
    gets(str);

    for (i = 0; i <= sizeof(str); i++)
    {
        if ((str[i] >= 'A') && (str[i] <= 'Z'))
        {
            str[i] += ('a' - 'A');
            cnt++;
        }
    }
    printf("바뀐 문장 : ");
    puts(str);
    printf("바뀐 문자 수 : %d", cnt);

    return 0;
}