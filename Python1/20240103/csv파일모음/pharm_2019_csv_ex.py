import csv

f = open("pharm_2019.csv", "r", encoding="utf-8")
fw = open("pharm_2019_mod.csv", "w", encoding="utf-8", newline='')

lines = csv.reader(f)
wr = csv.writer(fw)

data = ['약국명', '지역', '주소', '개설일자', '경도', '위도']
wr.writerow(data)

head = next(lines)

#print(head)
#['약국명', '지역', '주소', '개설일자', '경도', '위도']
#지역: 동대문구, 2019년도에 개설한 약국의 데이터개수

#동대문구 
cnt1 = 0
for i in lines:
        if "동대문구" in i[1] and '2019' in i[3]: 
                #cnt1 = cnt1+1
                #print(i)
                wr.writerow(i)

#print("동대문구", cnt1)

f.seek(0) #마우스 커서를 가장 상단에 올려놔라(초기화)
head = next(lines)

#종로구 
cnt2 = 0
for j in lines:
        if "종로구"  in j[1] and '2019' in j[3]:
                #cnt2 = cnt2 + 1
                #print(j)
                wr.writerow(j)
        
#print("종로구", cnt2)

    
f.close()
fw.close()
