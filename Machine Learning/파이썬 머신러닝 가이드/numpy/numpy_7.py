import numpy as np

# 선형대수 연산 - 행렬 내적과 전치 행렬 구하기
# 행렬 내적(행렬 곱)
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

dot_product = np.dot(A, B)
print('행렬 내적 결과:\n', dot_product)
print()

# 전치 행렬
C = np.array([[1, 2],
              [3, 4]])
transpose_mat = np.transpose(C)
print('C의 전치 행렬:\n', transpose_mat)