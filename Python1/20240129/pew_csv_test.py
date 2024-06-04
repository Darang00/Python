import pandas as pd
import numpy as np
import csv
import seaborn as sns

#넓은 데이터는 보기 안좋아서 데이터를 정규화
'''
pd.melt(df)
pandas.melt(frame, id_vars = None, value_vars = None, var_name=None,
            value_name='value', col_level = None, ignore_index=True)
#id_vars="위치를 유지할 열"
#value_vars = "가공할 열 이름"
#id_vars에 지정한 열 외에 나머지 열을 모두 가공한다면 따로 지정할 필요 X
#var_name = 가공되어 새로 따로 만들어지는 열 이름
#value_name=데이터 값 열 이름
'''

df = pd.read_csv("pew.csv")
print("df\n", df)

print("\n\ndf.index\n", df.index)#RangeIndex(start=0, stop=18, step=1)

print("\n\nmelt_test\n", df.melt(id_vars="religion", var_name="income", value_name="cnt"))

print("\n\ntail()\n", df.tail())
