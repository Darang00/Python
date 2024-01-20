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






