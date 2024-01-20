#%% 가격입력
price = int(input("가격: "))
print("%d" %(price*0.9))



#%% 사칙연산 (산술 연산자)
#정수 2개를 입력받고 덧셉, 뺄센, 곱셈, 나눗셈
num1 = int(input("first integer:"))
num2 = int(input("second integer:"))

addResult = num1 + num2
subResult = num1 - num2
mulResult = num1 * num2
divResult = num1 // num2    #몫
modResult = num1 % num2     #나머지

print("%d + %d = %d" %(num1, num2, addResult))
print("%d - %d = %d" %(num1, num2, subResult))
print("%d * %d = %d" %(num1, num2, mulResult))
print("%d // %d = %d" %(num1, num2, divResult))
print("%d %% %d = %d" %(num1, num2, modResult))












#%% 조건식
isOK = True
isNotOK = False
print(type(isOK)) #<class 'bool'>
print(type(isNotOK)) #<class 'bool'>

































