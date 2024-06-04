import matplotlib.pyplot as plt
import csv
f = open("month_temp.csv", "r", encoding="utf-8") #cp949
lines = csv.reader(f)

'''
month_temp
10월 01~ 10월 10일까지 날짜만 가져온 후 리스트에 저장
위 해당날짜의 최고기온을 가져온 후 리스트에 저장
위 해당 날짜의 최저기온을 가져온 후 리스트에 저장

matplotlib을 사용하여 1일부터 10일까지의 최고, 최저기온을 그래프로 시각화한다. 
'''


head = next(lines)

date = []
for i in lines:
    if int(i[1][8:])<=10 :
        date.append(i[1][8:])
        
#print(date)

f.seek(0)
head = next(lines)

maxTemp = []
for j in lines:
    maxTemp.append(j[4])

#print(maxTemp)

f.seek(0)
head = next(lines)

minTemp = []
for k in lines:
    if int(k[3]):
        minTemp.append(k[3])

#print(minTemp)

plt.xlabel("date")
plt.ylabel("degree")

plt.plot()

f.close



