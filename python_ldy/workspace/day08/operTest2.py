#%% (1) 관계 연산자
'''
isTrue = 10 == 11
     대입   관계
우선순위: 관계 먼저
'''
isTrue = 10 == 11
print("isTrue?", isTrue)   # False

isTrue = 10 != 11
print("isTrue?", isTrue)    # True




#%% (2)논리 연산자
isTrue = 10 == 11 and 10 > 1  #둘 다 참일때 참
#         (false)     (true)
print("isTrue?", isTrue)    # False


isTrue = 10 == 11 or 10 > 1 #둘 중 하나 참이면 참
#       (false)      (true)
print("isTrue?", isTrue)    #True






#%% (3) 단항 연산자
isTrue = 10 ==11
print(isTrue)       #False
print(not isTrue)   #True


















