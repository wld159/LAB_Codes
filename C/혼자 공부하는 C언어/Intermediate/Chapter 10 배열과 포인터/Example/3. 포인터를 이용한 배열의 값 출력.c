//
// Created by 권경호 on 2021/06/28.
//

#include <stdio.h>

int main(void)
{
    int ary[3] = {10, 20, 30};
    int *pa = ary;
    int i;

    printf("배열의 값 : ");
    for (i = 0; i < 3 ; i++)
    {
        printf("%d ", *pa);          // pa가 가리키는 배열 요소 출력
        pa++;                       // 다음 배열 요소를 가리키도록 pa 값 증가
    }

    return 0;
}