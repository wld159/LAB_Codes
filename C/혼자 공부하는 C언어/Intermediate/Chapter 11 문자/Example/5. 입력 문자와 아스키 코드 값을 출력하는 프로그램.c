//
// Created by 권경호 on 2021/06/29.
//

#include <stdio.h>

int main(void)
{
    int res;                        // scanf 함수의 반환값을 저장할 변수
    char ch;                        // 문자를 입력할 변수

    while (1)
    {
        res = scanf("%c", &ch);     // 문자 입력, <Ctrl> + <Z>를 누르면 -1 반환 (macOS의 경우, <Command> + <D>)
        if (res == -1) break;       // 반환값이 -1이면 반복 종료
        printf("%d ", ch);           // 입력된 문자의 아스키 코드 값 출력
    }

    return 0;
}