//
// Created by 권경호 on 2021/05/18.
//

#include <stdio.h>

int main(void)
{
    int kor = 3, eng = 5, mat = 4;                      // 국어, 영어, 수학의 학점 초기화
    int credits;                                        // 전체 학점을 저장할 변수
    int res;                                            // 연산 결과를 저장할 변수
    double kscore = 3.8, escore = 4.4, mscore = 3.9;    // 각 과목의 평점 초기화
    double grade;                                       // 평점의 평균을 저장할 변수

    credits = kor + eng + mat;                          // 전체 학점 계산
    printf("전체 학점 : %d\n", credits);
    grade = (kscore + escore + mscore) / 3;             // 평균의 평점 계산
    printf("평점 평균 : %.1lf\n", grade);
    res = (credits >= 10) && (grade >= 4.0);
    printf("(credits >= 10) && (grade >= 4.0) : %d\n", res);
    // 전체 학점이 10학점 이상이고 평점 평균이 4.0보다 크면 참이므로 결과는 1, 그렇지 않으면 거짓으로 결과는 0

    return 0;
}