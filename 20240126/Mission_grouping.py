import pandas as pd
import csv

data = ({
            'Team':['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings'],
            'Rank':[1, 2, 2, 3, 3, 4, ],
            'Year':[2014, 2015, 2014, 2015, 2014, 2015,23],
            'Points':[879, 789, 863, 673, 741, 812, 756, 788, 694]

            })
df = pd.DataFrame(data)
x = df.sort_values('Points', ascending: False) #Points를 내림차순으로 정렬
v = x.reset_index(drop=True) #index 재정의(순차적으로)

#데이터프레임명.sort_values(["열이름", "열이름"], ascending=False)
#ascending=False : 내림차순 정렬 ...
#ascending 없으면 default 로 오름차순 정렬

#데이터프레임명.reset_index(drop=True)

x = df.groupby('Team')
print(df.groupby('Team')['Points'].sum())
#'Team'별로 그룹화한 뒤 Points를 더해서 출력

#h = df.groupby(['Team', 'Year'])['Points'].sum()
point(h)
