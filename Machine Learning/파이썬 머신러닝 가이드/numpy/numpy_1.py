import numpy as np

# 넘파이 ndarray 개요
print("넘파이 ndarray 개요")

array1 = np.array([1, 2, 3]) # 1차원 array로 3개의 데이터를 가지고 있음
print('array1 type:', type(array1))
print('array1 array 형태:', array1.shape)

array2 = np.array([[1, 2, 3],
                  [2, 3, 4]]) # 2차원 array로, 2개의 Row와 3개의 Column을 가지고 있음
print('array2 type:', type(array2))
print('array2 array 형태:', array2.shape)

array3 = np.array([[1, 2, 3]]) # 2차원의 array로, 1개의 Row와 3개의 Column을 가지고 있음
print('array3 type:', type(array3))
print('array3 array 형태:', array3.shape)
print()

print('array1: {:0}차원, array2: {:0}차원, array3: {:0}차원'.format(array1.ndim, array2.ndim, array3.ndim))
print()