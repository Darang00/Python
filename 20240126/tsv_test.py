import pandas as pd
import csv

df = pd.read_csv("gapminder.tsv", sep="\t")
print(df)
#country continent  year  lifeExp       pop   gdpPercap
#국가, 대륙, 연도, 기대수명, 인구, gdp

'''
1. 연도별 기대수명 평균?
2. 기대수명, 인구, GDP 평균?
3. 대륙별 국가 개수?
'''

#1.
groupByYear = df.groupby('year')
print("groupByYear\n", groupByYear) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001E0013871A0>
groupByYear_lifeExp = groupByYear['lifeExp'].mean()
print("연도별 기대수명 평균\n", groupByYear_lifeExp)

print("------------------------------------------------------------------------")

#2.
groupByYear_AVG = groupByYear[['lifeExp',"pop","gdpPercap"]].mean()
print("연도별  기대수명 인구  GDP 평균\n", groupByYear_AVG)


#3.
groupByContinent = df.groupby('continent')
print("groupByContinent\n", groupByContinent)

popPerContinent = groupByContinent['country'].count()
print("대륙별 국가 개수\n", popPerContinent)


