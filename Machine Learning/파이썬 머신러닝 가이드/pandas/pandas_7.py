import pandas as pd
titanic_df = pd.read_csv('../Dataset/titanic_train.csv')

# 결손 데이터 처리하기
# isna()로 결손 데이터 여부 확인
print(titanic_df.isna().head(3))
print(titanic_df.isna().sum())

# fillna()로 결손 데이터 대체하기
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
print(titanic_df.head(3))
print()

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.isna().sum())
print()

# apply lambda 식으로 데이터 가공
def get_square(a):
    return a ** 2

print('3의 제곱은', get_square(3))

lambda_square = lambda x : x ** 2
print('3의 제곱은', lambda_square(3))
print()

a = [1, 2, 3]
squares = map(lambda x : x ** 2, a)
print(list(squares))

titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[['Name', 'Name_len']].head(3))
print()

titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
print(titanic_df[['Age','Child_Adult']].head(8))
print()

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x: 'Child' if x<= 15 else ('Adult' if x <= 60 else 'elderly'))
print(titanic_df['Age_cat'].value_counts())

# 나이에 따라 세분화된 분류를 수행하는 함수 생성.
def get_category(age):
    cat = ''
    if age <= 15: cat = 'Baby'
    elif age <= 12: cat = 'Child'
    elif age <= 18: cat = 'Teenager'
    elif age <= 25: cat = 'Student'
    elif age <= 35: cat = 'Young Adult'
    elif age <= 60: cat = 'Adult'
    else : cat = 'Elderly'

    return cat

# lambda 식에 위에서 생성한 get_category( ) 함수를 반환값으로 지정.
# get_category(X)는 입력값으로, 'Age' Column 값을 받아서 해당하는 cat 변환
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
print(titanic_df[['Age', 'Age_cat']].head())