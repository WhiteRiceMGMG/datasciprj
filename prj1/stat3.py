import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

student_data_math = pd.read_csv('chap3/student-mat.csv', sep=';')

print('平均値:', student_data_math['absences'].mean())
print('中央値:', student_data_math['absences'].median())
print('最頻値:', student_data_math['absences'].mode())

print('分散値:', student_data_math['absences'].var(ddof=0))
print('標準偏差:', student_data_math['absences'].std(ddof=0))

#要約統計量
print(student_data_math['absences'].describe())

#四分位範囲を求める
print(student_data_math['absences'].describe()[6] - student_data_math['absences'].describe()[4])

