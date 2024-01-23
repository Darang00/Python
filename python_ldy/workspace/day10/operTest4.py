#%% (1) 대소비교
#두 정수 입력받기
n1Msg = "첫 번째 정수: "
n2Msg = "두 번째 정수: "

num1 = int(input(n1Msg))
num2 = int(input(n2Msg))

#num1이 num2보다 크면 num1이 큰 값
#num1이 num2보다 작으면 num2가 큰 값
result = num1 if num1>num2 else num2
print("더 큰 값: {}".format(result))

#num2가 더 크거나, num1과 num2가 같으면 false쪽으로 이동한다.
#else 쪽(False쪽)에서 한 번 더 두 수가 같은지 판별한다.
#만약 두 수가 같다면 "두 수는 같습니다."
#만약 두 수가 같지 않다면 num2를 출력(더 큰 값)
result = num1 if num1>num2 else "X\n두 수가 같습니다" if num1==num2 else num2
print("더 큰 값: {}".format(result))



#%% (2)퀴즈게임
# =============================================================================
# 다음 중 프로그래밍 언어가 아닌것은?
# 1. JAVA
# 2. Python
# 3. C
# 4. candy
# =============================================================================

qMst = "다음 중 프로그래밍 언어가 아닌것은?"
choiceMsg = "1.JAVA\n2.Python\n3.C\n4.candy"
print(qMst+'\n'+choiceMsg)
answer = input("enter an answer:\n")

result = "정답입니다" if answer=='4' else '오답입니다'
print(result)









#%% 연산과 연결
print(10 + 9) #연산
print('10' + '9') #연결







