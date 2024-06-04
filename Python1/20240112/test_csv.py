import csv

'''
list, csv(읽기/쓰기)
'''

#month_temp.csv
#['지점', '일시', '평균기온(°C)', '최저기온(°C)', '최고기온(°C)']

#파일 오픈하고 file에다가 반환
file = open("month_temp.csv", "r", encoding="utf-8") #cp949

x = csv.reader(file)

cnt = 0


head = next(x)
print(head)
for i in x: #i에는 행 하나가 리스트 타입으로 저장됨
    #quiz: 최고기온이 27도 이상이었던 일자만 출력
    if float(i[4]) >27:
        cnt+=1
        print(i[1])
    

print(cnt)
file.close()
