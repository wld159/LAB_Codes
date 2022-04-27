//
// Created by 권경호 on 2021/05/18.
//

#include <stdio.h>

int main(void)
{
    int hour, min, sec;                 // 시, 분, 초를 저장할 변수
    double time = 3.76;                 // 시간 초기화

    hour = (int)time;                   // 형 변환으로 정수 부분만을 골라낸다.
    time -= (double)hour;               // 한 시간이 안되는 부분만을 다시 저장한다.
    time *= 60;                         // 분 단위로 환산
    min = (int)time;                    // 정수 부분만을 골라내어 분으로 저장한다.
    time -= (double)min;                // 일분이 안되는 부분만을 다시 저장한다.
    time *= 60;                         // 초 단위로 환산
    sec = (int)time;                    // 정수 부분만을 골라내어 초로 저장한다.
    printf("%.2lf시간은 %d시간 %d분 %d초입니다.\n", 3.76, hour, min, sec);    // 변환한 시간 출력

    return 0;
}