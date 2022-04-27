import pandas as pd
titanic_df = pd.read_csv('../Dataset/titanic_train.csv')

# 데이터 셀렉션 및 필터링
# DataFrame의 [] 연산자
print('단일 칼럼 데이터 추출:\n', titanic_df['Pclass'].head(3))
print('\n여러 칼럼의 데이터 추출:\n', titanic_df[['Survived', 'Pclass']].head(3))
# print('[] 안에 숫자 index는 KeyError 오류 발생:\n', titanic_df[0])

print(titanic_df[0:2])
print(titanic_df[titanic_df['Pclass'] == 3].head(3))

# DataFrame ix[] 연산자
# ix 메서드는 곧 사라질 예정_위치, 인덱스 기반 혼동 유발 가능
# print('칼럼 위치 기반 인덱싱 데이터 추출:', titanic_df.ix[0, 2])
# print('칼럼 명 기반 인덱싱 데이터 추출:', titanic_df.ix[0, 'Pclass'])성
print()

data = {'Name' : ['Chulmin', 'Eunkyung', 'Jinwoong', 'Soobeom'],
        'Year' : [2011, 2016, 2015, 2015],
        'Gender' : ['Male', 'Female', 'Male', 'Male']
        }
data_df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print(data_df)

# data_df를 reset_index()로 새로운 숫자형 인덱스를 생성
data_df_reset = data_df.reset_index()
data_df_reset = data_df_reset.rename(columns={'index':'old_index'})

# 인덱스값에 1을 더해서 1부터 시작하는 새로운 인덱스값 생성
data_df_reset.index += 1
# data_df_reset.ix[1, 1]
print()

# DataFrame iloc[] 연산자
print(data_df.iloc[0, 0])

# 다음 코드는 오류를 발생합니다.
# data_df.iloc['one', 0]

print(data_df_reset.iloc[0, 1])

# DataFrame loc[] 연산자
data_df.loc['one', 'Name']
data_df_reset.loc[1, 'Name']
print()

# 다음 코드는 오류를 발생합니다.
# data_df_reset.loc[0, 'Name']

# print('명칭 기반 ix slicing\n', data_df.ix['one': 'two', 'Name'], '\n')
print('명칭 기반 iloc sicing\n', data_df.iloc[0:1, 0], '\n')
print('명칭 기잔 loc slicing\n', data_df.loc['one': 'two', 'Name'])

print(data_df_reset.loc[1:2, 'Name'])
# print(data_df.ix[1:2, 'Name'])
print()

# 불린 인덱싱
titanic_boolean = titanic_df[titanic_df['Age'] > 60]
print(type(titanic_boolean))
print(titanic_boolean)

print(titanic_df[titanic_df['Age'] > 60][['Name', 'Age']].head(3))

print(titanic_df.loc[titanic_df['Age'] > 60, ['Name', 'Age']].head(3))

# 조건 부여
# 1. and 조걸일 때는 &
# 2. or 조건일 때는 |
# 3. not 조건일 때는 ~

# 나이가 60세 이상이고, 선실 등급이 1등급이며, 성별이 여성인 승객을 추출
print(titanic_df[(titanic_df['Age'] > 60) & (titanic_df['Pclass'] == 1) & (titanic_df['Sex'] == 'female')])

cond1 = titanic_df['Age'] > 60
cond2 = titanic_df['Pclass'] == 1
cond3 = titanic_df['Sex'] == 'female'
print(titanic_df[cond1 & cond2 & cond3])