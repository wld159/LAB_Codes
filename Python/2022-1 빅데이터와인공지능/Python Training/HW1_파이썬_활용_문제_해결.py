"""
2022-1 Big Data and Artifical Intelligence
Homework 1
Student ID: 2241007
Author: Gyeong Ho Kwon
"""
import math

# Input numbers
input_headers = ["첫 ", "두 ", "세 "]
list_nums = []
for i in range(0, 3):
    msg = input_headers[i] + "번째 수를 입력하세요: "
    num = int(input(msg))
    list_nums.append(num)
list_nums.sort()

# Assign numbers
num_min = list_nums[0]
num_mid = list_nums[1]
num_max = list_nums[2]

# Define variables for determining types of a triangle
hypotenuse = math.pow(num_max, 2)
other_sides = math.pow(num_min, 2) + math.pow(num_mid, 2)

print("( --> 결과)")
if num_max < num_min + num_mid:
    if hypotenuse > other_sides:
        # Obtuse triangle
        print("둔각삼각형입니다.")
    elif hypotenuse == other_sides:
        # Right-angled traingle
        print("직각삼각형입니다.")
    else:
        # Acute traingle
        print("예각삼각형입니다.")
else:
    print("삼각형이 아닙니다.")

# Create empty list for appending mupliples under certain condition
list_multiples = []

for i in range(num_min + 1, num_max):
    if i % 3 == 0:
        list_multiples.append(i)

if list_multiples == []:
    print(f"{num_min}와 {num_max}사이 3의 배수는 없습니다.")
else:
    print(f"{num_min}와 {num_max}사이 3의 배수는 {' '.join(map(str, list_multiples))}이고 총 {len(list_multiples)}개입니다.")