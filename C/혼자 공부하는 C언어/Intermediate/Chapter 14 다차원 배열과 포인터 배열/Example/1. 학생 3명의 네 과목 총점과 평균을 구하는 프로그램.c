//
// Created by 권경호 on 2021/07/02.
//

#include <stdio.h>

int main(void)
{
    int score[3][4];                            // 3명의 네 과목 점수를 저장할 2차원 배열 선언
    int total;                                  // 총점
    double avg;                                 // 평균
    int i, j;                                   // 반복 제어 변수

    for (i = 0; i < 3; i++)                     // 학생 수 만큼 반복
    {
        printf("4과목의 점수 입력 : ");                // 입력 안내 메시지
        for (j = 0; j < 4; j++)                 // 과목 수 만큼 반복
        {
            scanf("%d", &score[i][j]);          // 점수 입력
        }
    }

    for (i = 0; i < 3; i++)                     // 학생 수 만큼 반복
    {
        total = 0;                              // 학생이 바뀔 때마다 0으로 초기화
        for (j = 0; j < 4; j++)                 // 과목 수 만큼 반복
        {
            total += score[i][j];               // 학생별로 총점 누적
        }
        avg = total / 4.0;                      // 평균 계산
        printf("총점 : %d, 평균 : %.2lf\n", total, avg);            // 총점, 평균 출력
    }

    return 0;
}