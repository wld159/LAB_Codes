"""
자동 판매기를 시뮬레이션하는 프로그램을 작성해보자.
자동 판매기는 사용자로부터 투입한 돈과 물건값을 입력받는다.
물건값은 100원 단위라고 가정한다.
프로그램은 잔돈을 계산하여 출력한다.
자판기는 동전 100원, 100원짜리만 가지고 있다고 가정하자.
투입한 금액과 물건값을 입력으로 받아 거스름돈으로 500원 동전 몇 개와
100원 동전 몇 개를 내어 보내면 되는지 계산하는 프로그램을 작성하라.
"""

money = int(input("투입한 돈: "))
price = int(input("물건값: "))

change = money - price
print("거스름돈: ", change)
coin500s = change // 500 # 500으로 나누어서 몫이 500원 동전의 개수
change = change % 500 # 500으로 나눈 나머지를 계산한다.
coin100s = change // 100 # 100으로 나누어서 몫이 100원짜리의 개수

print(">>> 동전의 개수 출력")
print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)