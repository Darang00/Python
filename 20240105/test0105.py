import random

'''
for i in range(3):
    print(random.random())
    random.randrange(1, 10, 2) #1이상, 10미만의 난수, 2칸씩 띄어서 출력 #(start, end, step)
    random.randint(1, 5) --> end 범위 포함
    random.choice(리스트, 튜플, 문자)
    random.shuffle(리스트) #리스트에 있는거 랜덤으로 순서 배열해서 리스트 인자에 다시 저장함.

'''

'''
data = ["가위", "바위", "보"]
for i in range(3):
    random.shuffle(data) 
    print(data)
'''


'''
주사위 게임 만들기
사용자 주사위: 1~6
컴퓨터 주사위: 1~6

if 변수, randint(start, end)

사용자 win, 컴퓨터 win

Update
100번을 반복하면서 사용자가 NO 입력하면 주사위 게임 종료.

for i in rang(100):
    user = random.randint(1, 6)
    com = random.randint(1, 6)

    if user>com:
        #print("You win")
        me_cnt +=1
    elif user< com:
        #print("Com win")
        com_cnt +=1
    else:
        Q = input("게임종료를 원하면 No를 입력해라: ")
        if Q == "NO" or
'''






