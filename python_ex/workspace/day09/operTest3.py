#%% 실수의 오류
print(0.1 + 0.2) #0.30000000000000004 (끝에 쓰레기값 붙음)
print(0.1 + 0.2 == 0.3) #False
print("%.1f" %0.3)
print("%.1f" %(0.1 + 0.2) == "%.1f" %0.3) #True




#%% 실수의 오류 해결1
import math 

print(math.isClose(0.1+0.2, 0.3))


#%% 실수의 오류 해결2

from decimal import Decimal

print(float(Decimal('0.1') + Decimal('0.2')) == 0.3) #True



