import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

student_data_math = pd.read_csv('chap3/student-mat.csv', sep=';')

#plt.boxplot(student_data_math['G1'])
#plt.grid(True)
#plt.show()

#plt.boxplot(student_data_math['absences'])
#plt.grid(True)
#plt.show()

#plt.boxplot([student_data_math['G1'], student_data_math['G2'], student_data_math['G3']])
#plt.grid(True)
#plt.show()

#print(student_data_math['absences'].std(ddof=0) / student_data_math['absences'].mean())

#print(student_data_math.std(ddof=0) / student_data_math.mean())

plt.plot(student_data_math['G1'], student_data_math['G3'], 'o')
plt.ylabel('G3 grade')
plt.xlabel('G1 grade')
plt.grid(True)
#plt.show()

#ピアソン関数で２変数の相関係数を算出できる
print(sp.stats.pearsonr(student_data_math['G1'], student_data_math['G3']))