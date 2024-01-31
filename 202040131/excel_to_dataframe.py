import mata
import seaborn as sns
import numpy as np
import pandas as pd

import openpyxl

excel="엑셀파일의 저장경로"
df = pd.read_excel(excel)
print(df)
