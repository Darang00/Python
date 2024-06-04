import csv

file = open("classtest.csv", "r", encoding="utf-8") #csv 파일을 읽기 모드로 열기
lines = csv.reader(file)



for i in lines:
    print(i)


file.close()
