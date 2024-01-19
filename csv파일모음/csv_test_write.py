import csv
#open(): 파일 열기 , close(): 파일 닫기
f = open("month_temp.csv", "r", encoding="UTF-8")
fw = open("month_oct.csv", "w", encoding="UTF-8", newline='') #마지막에 newline='' 함으로써 줄바꿈 제거
#파일명.확장자, 읽기/쓰기모드, 문자종류
#"test.csv" 파일 객체가 f 에 저장됨
#본 소스코드파일이 저장된 위치에 열고자 하는 .csv 파일이 존재해야 정상적으로 실행됨.

lines = csv.reader(f)
wr = csv.writer(fw)

data = ["일자", "최저기온", "최고기온", "일교차"]
wr.writerow(data)

head = next(lines)

#print("%s %s %s %s"%("일자", "최저기온", "최고기온", "일교차"))

for i in lines:
    tmp = float(i[4]) - float(i[3])
    tmp = format(tmp, ".1f") #소수점 첫 째자리까지만 표현 
    wr.writerow([i[1], float(i[3]), float(i[4]), tmp])

f.close()
fw.close()
    
