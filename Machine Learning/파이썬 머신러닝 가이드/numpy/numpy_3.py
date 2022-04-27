import numpy as np

# ndarray를 편리하게 생성하기 - arrange, zeros, ones
print("ndarray를 편리하게 생성하기 - arrange, zeros, ones")

sequence_array = np.arange(10) # arange : 0부터 함수 인자 값 -1까지의 값을 순차적으로 ndarray 데이터값으로 변환
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

zero_array = np.zeros((3, 2), dtype='int32') # zero : 함수 인자로 tuple 형태의 shape 값을 입력하면,\
                                            # 모든 값을 0으로 채운 해당 shape을 가진 ndarray를 반환
print(zero_array)
print(zero_array.dtype, zero_array.shape)

one_array = np.ones((3, 2)) # ones 함수 인자로 튜플 형태의 shape 값을 입력하면, 모든 값을 1로 채운 해당 shape를 가진 ndarray를 반환
print(one_array)
print(one_array.dtype, one_array.shape)