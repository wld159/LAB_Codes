//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>

int main(void)
{
    int age;                        // 나이를 저장할 변수
    char name[20];                  // 이름을 저장할 배열

    printf("나이 입력 : ");
    scanf("%d", &age);              // scanf로 함수로 나이 입력
    fgetc(stdin);
    printf("이름 입력 : ");
    gets(name);
    printf("나이 : %d, 이름 : %s\n", age, name);

    return 0;
}