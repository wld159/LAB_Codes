//
// Created by 권경호 on 2021/05/15.
//

#include <stdio.h>

int main(void)
{
    printf("Be happy\n");               // "Be happy"를 출력하고 줄을 바꿈(\n)
    printf("12345678901234567890\n");   // "화면에 열 번호를 출력하고 줄을 바꿈(\n)
    printf("My\tfriend\n");
    // "My"를 출력하고 탭 위치로 이동(\t) 후에 "friend"를 출력하고 줄을 바꿈(\n)
    printf("Goot\bd\tchance\n");
    // t를 d로 바꾸고 탭 위치로 이동(\t) 후에 "chance"를 출력하고 줄을 바꿈(\n)
    printf("Cow\rW\a\n");
    // 맨 앞으로 이동(\r)go C를 W로 바꾸고 벨소리(\a)를 내고 줄을 바꿈(\n)

    return 0;
}