'''
#%%
for i in range(5, 12):
    print('Hello', i);

#%%
data = [1, 2, 3, 4, 5]
for i in data:
    print(i)
'''

'''
#%%
data = (1, 2, 3, 4, 5)
for i in data:
    print(i)

data = [1, 'hello', 0.5]
for i in data:
    print(i, end=' ')
'''

'''
data=[]
for i in range(3):
    print(i, end=' ')
    data.append(input("input: "))

    print(data)
'''

'''
# 두 개의 정수를 입력받고 두 정수 사이의 숫자를 출력한다.
#입력 예시) 3 8
#출력 예시) 3 4 5 6 7 8
# 방법1
x=int(input())
y=int(input())
for i in range(x, y+1):
        print(i)

#방법2 이거는 모길래 에러가 날까..
x,y = map(int, input("input int: ").split())
for i in range(x, y+1):
        print(i)

'''
#1부터 100까지의 합을 구한 후 출력한다.
#1부터 100까지의 짝수 합과 홀수 합을 출력한다.
#1부터 100까지의 홀수만 출력한다. (continue) 사용
#사용자로부터 10개의 데이터를 순서대로 입력받고 사용자가 -1을 입력하면 반복문을 탈출한다.
'''
1번문제
x=0
for i in range(1, 11):
    x+= i
    print(x)
'''

'''
#2번 짝
add=0
for i in range(1, 101):
    if i%2 ==0:
        add = add + i

print(add) #2550
'''

'''
#2번 홀
add=0
for i in range(1, 101):
    if i%2 ==1:
        add = add + i

print(add) #2500
'''

'''
#3번
for i in range(1, 101):
    if i%2 ==0:    #짝수 일 때
        continue   #스킵하고 넘어감
    print(i)         #짝수 아닌거는 프린트
'''

'''
#4번
for i in range(10):
    x=int(input())
    if x == -1:
        break
'''


'''
b = (1, 2, 3)
b[0] = 5
print(b) #TypeError: 'tuple' object does not support item assignment
'''


#중첩 반복문
#반복문은 횟수가 끝나기 전까지 절대 빠져나가지 않는다.

#1*1 형태로 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(i , '*' , j , '=', i*j)


    








    
