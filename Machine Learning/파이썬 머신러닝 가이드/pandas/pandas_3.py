import pandas as pd
titanic_df = pd.read_csv('../Dataset/titanic_train.csv')

# DataFrame의 Column 데이터 세트 생성과 수정
titanic_df['Age_0'] = 0
print(titanic_df.head(3))

titanic_df['Age_by_10'] = titanic_df['Age'] * 10
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
print(titanic_df.head(3))

titanic_df['Age_by_10'] += 100
print(titanic_df.head(3))

# DataFrame의 데이터 삭제
titanic_drop_df = titanic_df.drop('Age_0', axis=1)
print(titanic_drop_df.head(3))

print(titanic_df.head(3))

drop_result = titanic_df.drop(['Age_0', 'Age_by_10', 'Family_No'], axis=1, inplace=True)
print('inplace=True로 drop 후 반환된 값:', drop_result)
titanic_df.head(3)

pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 15)
print('#### before axis 0 drop ####')
print(titanic_df.head(3))
titanic_df.drop([0, 1, 2], axis=0, inplace=True)

print('#### after axis 0 drop ####')
print(titanic_df.head(3))