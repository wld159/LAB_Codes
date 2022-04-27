import pandas as pd
titanic_df = pd.read_csv('../Dataset/titanic_train.csv')

# Index 객체
# Index 객체 추출
indexes = titanic_df.index
print(indexes)

# Index 객체를 실제 값 array로 변환
print('Index 객체 array값:\n', indexes.values)

print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])

series_fair = titanic_df['Fare']
print('Fair Series max 값:', series_fair.max())
print('Fair Series sum 값:', series_fair.sum())
print('sum() Fair Series:', sum(series_fair))
print('Far Series + 3:\n', (series_fair + 3).head(3))

titanic_reset_df = titanic_df.reset_index(inplace=False)
print(titanic_reset_df.head(3))
print()

print('### before reset_index ###')
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입', type(value_counts))
new_value_counts = value_counts.reset_index(inplace=False)
print('### After reset_index ### ')
print(new_value_counts)
print('new_value_counts 객체 변수 타입:', type(new_value_counts))