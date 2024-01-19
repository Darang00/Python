#딕셔너리: 키와 값을 가지고 있는 자료형
'''
딕셔너리 형태: { 중괄호 }로 감싸져 있음 

'''

#딕셔너리 인덱싱
data = { "메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]
            }

print(data["메로나"][0])


#딕셔너리 데이터 추가 
data = { "메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]
            }
data["구구콘"] = [700, 10]


#딕셔너리 keys() 메서드
data = { "메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]
            }
key = list(data.keys()) #list


#딕셔너리 values() 메서드
data = { "메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]
            }
values = list(data.values()) #list


#딕셔너리 update() 메서드
data = { "메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]
            }
data1 = {"팥빙수":1000, "탱크바": 2000}
data.update(data1)
print("update()", data)
print("type", type(data)) #type <class 'dict'>




#딕셔너리 zip 과 dic
keys = ("banana", "apple", "peach")
values = (1000, 2000,3000)
print("keys", type(keys))
print("values", type(values))
data = dict(zip(keys, values))
print("zip 과 dic", data)
print("type", type(data))



'''
zip은 동일한 개수로 이뤄진 데이터타입을 순서에맞게 묶어준다.
dict()는 특정 데이터를 딕셔너리로 변환한다.
'''
#dictionary.get()
data = { "메로나": 300,
              "비비빅": 400,
              "죠스바": 250
            }
print("data.get( )",data.get("메로나")) #300
print("data.get( )",data.get("수박바")) #None
print("data.get( )",data.get("수박바", 0)) #NVL과 동일한 기능인듯 : 0
#print(data["수박바"]) #KeyError: '수박바'

print()
print("---------------------------------------------------------------------")
print()


#딕셔너리 로그인문제 해결
#   ID:PW
signInInfo = {
                "kim":'123',
                "Lee":'456',
                "Park":'789'
                
            }
'''
1. 
ID를 키로, PW를 값으로 설정한다.
사용자로부터 ID를 입력받고 PW를 입력받은 뒤
딕셔너리에 있다고 판단 후 있다면 사용자가 입력한 PW가 맞는지 확인.
ID와 PW가 모두 동일하면 로그인 성공 메시지 출력

2. 5개의 id를 입력받고 리스트에 저장
    5개의 pw를 입력받고 리스트에 저장

    zip 함수와 dict 함수를 사용하여 하나의 딕셔너리로 만든다.
'''
'''
#1.
userID = input("enter your ID: ")
userPW = input("enter your PW: ")

#1.1
if signInInfo.get(userID, "0") != "0":
    if signInInfo.get(userID) == userPW:
        print("로그인성공")

    else:
        print("로그인실패")

else:
    print("로그인실패")

#1.2
if userID in signInInfo.keys():
    if signInInfo.get(userID) == userPW:
        print("로그인성공")

    else:
        print("로그인실패")

else:
    print("존재하지 않는 ID")
'''
'''
#1.3 횟수제한
for i in range(3):
    userID = input("enter your ID: ")
    userPW = input("enter your PW: ")
    
    if userID in signInInfo.keys():
        if signInInfo.get(userID) == userPW:
            print("로그인성공")
            break

        else:
            print("로그인실패")

    else:
        print("존재하지 않는 ID") 
'''   

#2. input().split() ???
'''
반복문 안돌고 한번에 아이디 다 받아서 리스트에 저장
x=input("enter your ID:").split(",") 
print(x)

#딕셔너리 zip 과 dic
keys = ("banana", "apple", "peach")
values = (1000, 2000,3000)
data = dict(zip(keys, values))
print("zip 과 dic", data)
print("type", type(data))
'''
print("회원들 계정 등록 시작")
idList = [0 for i in range(5)]

pwList = [0 for i in range(5)]

for i in range(5):
    idList[i] = input("enter your ID:")

idListKey = tuple(idList)
#print("idListKey", idListKey)

for i in range(5):
    pwList[i] = input("enter your PW:")

pwListValue = tuple(pwList)
#print("pwListValue", pwListValue)

data = dict(zip(idListKey, pwListValue))


#로그인에 적용해보기
print("로그인시작")
for i in range(3):
    userID = input("enter your ID: ")
    userPW = input("enter your PW: ")
    
    if userID in data.keys():
        if data.get(userID) == userPW:
            print("로그인성공")
            break

        else:
            print("로그인실패")

    else:
        print("존재하지 않는 ID") 




















































































