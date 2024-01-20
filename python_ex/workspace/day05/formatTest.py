#%% format test
data  = 10
data2 = "%d" %100
print("data : %d" %data);
print(type(data2))
print(data2);

#%% format test2
# 문자열값.format()
# A.B : A 안에 B
data1 = 10
data2 = 10.4231
data3 = 'A'
data4 = "ABC"

print("data1 : {}".format(data1))
print("data1 : {}\ndata2 : {}".format(data1, data2))
print("data3 : %s" %data3)
print("data3 : %c" %data3)
print("data4: %s" %data4) #(정상)
#print("data4: %c" %data4) #오류남(타입에러)
print("data : %c" %63) #?
print("data : %c" %64) #@
print("data : %c" %65) #A
print("data : %c" %66) #B
print("data : %c" %67) #C

# 아스키 코드
print("아스키코드a : %c" %97) #a

#%% 자동 형변환
# // : 몫 연산자
print(10/3) # 3.3333333333333335
print(10//3) # 3
print(10//3.0) #3.0

#%% 강제 형변환
print(float(10)) # 10.0
print(float(10)//3) # 3.0
