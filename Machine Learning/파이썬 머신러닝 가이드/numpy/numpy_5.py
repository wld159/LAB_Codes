import numpy as np

# 넘파이의 ndarray의 데이터 세트 선택하기 - 인덱싱(Indexing)
print("넘파이의 ndarray의 데이터 세트 선택하기 - 인덱싱(Indexing)")

# 단일 값 추출
# 1부터 9까지의 1차원 ndarray 생성
array1 = np.arange(start=1, stop=10)
print('array1:', array1)
# index는 0부터 시작하므로 array1[2]는 3번째 index 위치의 데이터값을 의미
value = array1[2]
print('value:', value)
print(type(value))
print('맨 뒤의 값:', array1[-1], ' 맨 뒤에서 두 번째 값:', array1[-2])

array1[0] = 9
array1[8] = 0
print('array1:', array1)

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)

print('(row=0, col=0) index 가리키는 값:', array2d[0, 0])
print('(row=0, col=1) index 가리키는 값:', array2d[0, 1])
print('(row=1, col=0) index 가리키는 값:', array2d[1, 0])
print('(row=2, col=2) index 가리키는 값:', array2d[2, 2])
print()

# 슬라이싱
array2 = np.arange(start=1, stop=10)
array3 = array2[0:3]
print(array3)
print(type(array3))
print()

array4 = array2[:3]
print(array4)

array5 = array2[3:]
print(array5)

array6 = array2[:]
print(array6)
print()

print('array2d:\n', array2d)

print('array2d[0:2, 0:2] \n', array2d[0:2, 0:2])
print('array2d[1:3, 0:3] \n', array2d[1:3, 0:3])
print('array2d[1:3, :] \n', array2d[1:3, :])
print('array2d[:, :] \n', array2d[:, :])
print('array2d[:2, 1:] \n', array2d[:2, 1:])
print('array2d[:2, 0] \n', array2d[:2, 0])
print()

print(array2d[0])
print(array2d[1])
print('array2d[0] shape:', array2d[0].shape, 'array2d[1] shape:', array2d[1].shape)

# 팬시 인덱싱
array7 = array2d[[0, 1], 2]
print('array2d[[0, 1], 2] =>', array7.tolist())

array8 = array2d[[0, 1], 0:2]
print('array2d[[0, 1], 0:2] =>', array8.tolist())

array9 = array2d[[0, 1]]
print('array2d[[0, 1]] =>', array9.tolist())
print()

# 불린 인덱싱
# [ ] 안에 array1d > 5 Boolean indexing을 적용
array10 = array1d[array1d > 5]
print('array1d > 5 불린 인덱싱 결과 값 :', array10)

print(array1d > 5)

boolean_indexes = np.array([False, False, False, False, False, True, True, True, True])
array11 = array1d[boolean_indexes]
print('불린 인덱스로 필터링 결과 :', array11)

indexes = np.array([5, 6, 7, 8])
array12 = array1d[indexes]
print('일반 인덱스로 필터링 결과 :', array12)