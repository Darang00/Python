#6102 numpy_arange
'''
1. 10, 11, 12, ..., 48, 49 원소를 갖는 넘파일 배열을 출력하시오.

2. 위 배열을 역순 배열로 만들어 출력하시오.

3. 0~8의 원소를 갖는 3x3 행렬을 만들어 출력하시오. - reshape 활용

4. [1,2,0,0,4,0]에서 0이 아닌 원소의 위치를 출력하시오. - nonzero 활용

5. 3x3의 단위 행렬을 만들어서 출력하시오. - eye 활용
'''

#1.
import numpy as np

array_np = np.zeros(40, dtype=np.int32)

print(len(array_np))
#for i in 

