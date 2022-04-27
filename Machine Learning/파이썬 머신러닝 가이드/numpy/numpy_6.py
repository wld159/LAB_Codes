import numpy as np
# 행렬의 정렬 - sort()와 argsort()
print("행렬의 정렬 - sort()와 argsort()")

# 행렬 정렬
org_array = np.array([3, 1, 9, 5])
print('원본 행렬', org_array)
# np.sort()로 정렬
sort_array1 = np.sort(org_array)
print('np.sort() 호출 후 반환된 정렬 행렬:', sort_array1)
print('np.sort() 호출 후 반환된 원본 행렬:', org_array)
# ndarray.sort()로 정렬
sort_array2 = org_array.sort()
print('org_array.sort() 호출 후 반환된 행렬:', sort_array2)
print('org_array.sort() 호출 후 원본 행렬:', org_array)

sort_array1_desc = np.sort(org_array)[::-1]
print('내림차순으로 정렬', sort_array1_desc)

array2d = np.array([[8, 12],
                    [7, 1]])

sort_array2_axis0 = np.sort(array2d, axis=0)
print('Row 방향으로 정렬:\n', sort_array2_axis0)

sort_array2_axis1 = np.sort(array2d, axis=1)
print('Column 방향으로 정렬:\n', sort_array2_axis1)
print()

# 정렬된 행렬의 인덱스를 반환하기
sort_indices = np.argsort(org_array)
print(type(sort_indices))
print('행렬 정렬 시 원본 행렬의 인덱스:', sort_indices)
sort_indices_desc = np.argsort(org_array)[::-1]
print('행렬 내림차순 정렬 시 원본 행렬의 인덱스:', sort_indices_desc)
print()

name_array = np.array(['John', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array = np.array([78, 95, 84, 98, 88])

sort_indices_asc = np.argsort(score_array)
print('성적 오름차순 정렬 시 score_array의 인덱스:', sort_indices_asc)
print('성적 오름차순으로 name_array의 이름 출력', name_array[sort_indices_asc])