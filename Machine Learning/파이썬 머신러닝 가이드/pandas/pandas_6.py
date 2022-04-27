import pandas as pd
titanic_df = pd.read_csv('../Dataset/titanic_train.csv')

# 정렬, Aggregation 함수, GroupBy 적용
# DataFrame, Series의 정렬 - sort_values()
titanic_sorted = titanic_df.sort_values(by=['Name'])
print(titanic_sorted.head(3))
print()

titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
print(titanic_sorted.head(3))
print()

# Aggregation 함수 적용
print(titanic_df.count())
print(titanic_df[['Age','Fare']].mean())
print()

# groupby() 적용
titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))
titanic_groupby = titanic_df.groupby('Pclass').count()
print(titanic_groupby)
print()

titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId', 'Survived']].count()
print(titanic_groupby)
print()

print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))
print()

agg_format = {'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
print(titanic_df.groupby('Pclass').agg(agg_format))