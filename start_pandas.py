#판다스는 데이터 처리에 최적화된 패키지
import os, re
import numpy as np
import pandas as pd

data = {'name': ['Mask', 'Jane', 'Chris', 'Ryan'],
        'age' : [33, 32, 44, 42],
        'score': [91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)
print()
print(df)
print()
print(df.sum())
print()
print(df.mean())
print()

print(df.score)
print()