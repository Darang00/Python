import pandas as pd
import csv

df = pd.read_csv("high_school_2019.csv")
#csv 파일을 불러와서 바로 데이터 프레임 객체로 변환해서 저장한다.

print(df)
print("type(df)", type(df)) #<class 'pandas.core.frame.DataFrame'>

#print(df.head())           #앞에서부터 5개 행만 출력 (default n= 5)
#print(df.head(n =10))  #앞에서부터 10개 행만 출력
#print(df.tail())               #뒤에서부터 5개 행만 출력 (default n= 5)
#print(df.tail(n = 10))     #뒤에서부터 10개 행만 출력


'''
1. 1학년 학급수 1학년 학생수 2학년 학급수 2학년 학생수 3학년 학급수 3학년 학생수

2. 각 학년별 총학생 구하고 출력하기.
    1학년총학생수   2학년총학생수   3학년 총학생수
    
'''

print("1.--------------------------------------------")
df_year = df.iloc[:, 2:]
print("df_year", df_year)
print("type(df_year)",type(df_year)) #<class 'pandas.core.frame.DataFrame'>

print("2.1--------------------------------------------")
tot = df_year.sum(axis=0)
print("tot\n", tot)
print("type(tot)",type(tot)) #type(tot) <class 'pandas.core.series.Series'>
print("tot.iloc[1:7:2]\n", tot.iloc[1:7:2]) #iloc[시작행의 index: 마지막 행의 index: 간격]
print("2.2--------------------------------------------")
print(tot.iloc[1:7:2].index.values)
print(tot.iloc[1:7:2].values)
print("type(tot.iloc[1:7:2].index)", type(tot.iloc[1:7:2].index)) #<class 'pandas.core.indexes.base.Index'>
print("type(tot.iloc[1:7:2].index.values)",type(tot.iloc[1:7:2].index.values)) #<class 'numpy.ndarray'>
print("type(tot.iloc[1:7:2].values)",type(tot.iloc[1:7:2].values)) #<class 'numpy.ndarray'>
print("2.3--------------------------------------------")
print(tot.iloc[[1, 3, 5]])

'''
print("\n1학년총학생수   2학년총학생수   3학년 총학생수")
std_tot = []
for i in range(3):
    x =tot.iloc[2*i+1]
    std_tot.append(x)

print(std_tot)
'''
