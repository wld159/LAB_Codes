import numpy as np
import pandas as pd

# DataFrame과 리스트, 딕셔너리, 넘파이 ndarray 상호 변환
# 넘파이 ndarray, 리스트, 딕셔너리를 DataFrame으로 변환하기

col_name1 = ['col1']
list1 = [1, 2, 3]
array1 = np.array(list1)
print('array1 shape:', array1.shape)

# 리스트를 이용해 DataFrame 생성.
df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DataFrame:\n', df_list1)

# 넘파이 ndarray를 이용해 DataFrame 생성.
df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DataFrame:\n', df_array1)

# 3개의 Column명이 필요함.
col_name2 = ['col1', 'col2', 'col3']

# 2행 X 3열 형태의 리스트와 ndarray를 생성한 뒤 이를 DataFrame으로 변환.
list2 = [[1, 2, 3],
         [11, 22, 33]]
array2 = np.array(list2)
print('array2 shape:', array2.shape)

df_list2 = pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 DataFrame:\n', df_list2)

df_array2 = pd.DataFrame(array2, columns=col_name2)
print('2차원 ndarray로 만든 DataFrame:\n', df_array2)

# Key는 문자열 Column명으로 매핑, Value는 리스트 형(또는 ndarray) 칼럼 데이터로 매핑
dict = {'col1':[1, 11], 'col2':[2, 22], 'col3':[3, 33]}
df_dict = pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame:\n', df_dict)

# DataFrame을 넘파이 ndarray, 리스트, 딕셔너리로 변환하기
# DataFrame을 ndarray로 변환
array3 = df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
print(array3)

# DataFrame을 리스트로 변환
list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
print(list3)

# DataFrame을 딕셔너리로 변환
dict3 = df_dict.to_dict('list')
print('\ndf_dict.todict() 타입:', type(dict3))
print(dict3)