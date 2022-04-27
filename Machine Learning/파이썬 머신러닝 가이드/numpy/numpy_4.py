import numpy as np

# ndarray의 차원과 크기를 변경하는 reshape()
print("ndarray의 차원과 크기를 변경하는 reshape()")

array1 = np.arange(10) # 1차원 형태의 array
print('array1:\n', array1)

array2 = array1.reshape(2, 5) # 2 Row X 5 Column 형태로 변환
print('array2:\n', array2)

array3 = array1.reshape(5, 2) # 5 Row X 2 Column 형태로 변환
print('array3:\n', array3)
print()

array4 = array1.reshape(-1, 5) # 고정된 5개의 Column에 맞는 Row를 자동으로 새롭게 생성해 변환
print('array4 shape:', array4.shape)

array5 = array1.reshape(5, -1) # 고정된 5개의 Row에 맞는 Column을 자동으로 새롭게 생성해 변환
print('array5 shape:', array5.shape)
print()

array6 = np.arange(8)
array3d = array6.reshape((2, 2, 2))
print('array3d:\n', array3d.tolist())

# 3차원 ndarray를 2차원 ndarray로 변환
array7 = array3d.reshape(-1, 1)
print('array7:\n', array7.tolist())
print('array7 shape', array7.shape)

# 1차원 ndarray를 2차원 ndarray로 변환
array8 = array6.reshape(-1, 1)
print('array8:\n', array8.tolist())
print('array8 shape', array8.shape)