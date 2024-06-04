'''
import module

# . 접근연산자
module.get_name("Lho")
module.get_name2("Dayeong")
module.get_name3("Shaxa")
print(module.x)
'''



'''
from module import get_name, get_name2, get_name3
get_name("Lho")
get_name2("Dayeong")
get_name3("Shaxa")
'''


'''
from module import *
get_name("Lho")
get_name2("Dayeong")
get_name3("Shaxa")
print(x)
'''


''' 모듈 이름이 너무 긴 경우..
import dayeongLho

dayeongLho.get_name("Lho")
dayeongLho.get_name2("Dayeong")
dayeongLho.get_name3("Shaxa")
print(dayeongLho.x)
'''



'''
# import 하는 모듈 이름에 별칭 부여하여 사용 가능 
import dayeongLho as lho
lho.get_name("Lho")
lho.get_name2("Dayeong")
lho.get_name3("Shaxa")
print(lho.x)
'''





'''
cal.py

각 사칙 연산의 함수를 정의한다.
(+, -, *, /, //, %)

main.py
사칙연산의 함수를 호출하고 데이터(인자)를 전달한다.
출력은 메인 파일에서 연산의 결과를 출력한다.

'''





