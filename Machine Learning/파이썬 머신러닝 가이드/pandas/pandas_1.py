import pandas as pd

# 판다스 시작 - 파일을 DataFrame으로 로딩, 기본 API
titanic_df = pd.read_csv('../Dataset/titanic_train.csv')
print('titanic 변수 type:', type(titanic_df))
print(titanic_df)
print()

print(titanic_df.head(3))
print('DataFrame 크기:', titanic_df.shape)
print()

print(titanic_df.info())
print()

print(titanic_df.describe())
print()

value_counts = titanic_df['Pclass'].value_counts()
print(type(value_counts))
print(value_counts)
print()

titanic_pclass = titanic_df['Pclass']
print(type(titanic_pclass))
print()

print(titanic_pclass.head())