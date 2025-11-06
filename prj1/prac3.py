import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import scipy.linalg as linalg
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy.optimize import newton
import math

#*************************************************************************************#
#3-1 ポルトガル語のデータを読みこんで，要約統計量を示せ．                             #
#*************************************************************************************#
student_por_data = pd.read_csv('chap3/student-por.csv', sep=';')
print(student_por_data.head())
print(student_por_data.info())
print(student_por_data['school'].head())
print(student_por_data['absences'].head())
print(student_por_data['absences'].describe())

#*************************************************************************************#
#3-2 数学のデータとポルトガル語のデータをマージ．                                     #
# ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Menu', 'Fedu', 'Mjob',   #
#  'Fjob', 'reason', 'nursery', 'internet']                                           #
# suffixes=('_math', '_por')                                                          #
#*************************************************************************************#
student_mat_data = pd.read_csv('chap3/student-mat.csv', sep=';')
join_keys =  ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob',
              'Fjob', 'reason', 'nursery', 'internet']
student_merge = pd.merge(student_por_data,
         student_mat_data,
         on=join_keys,
         suffixes=('_math', '_por'))
print(student_merge.head())

#**************************************************************************************#
#3-3 マージしたデータについて，いくつかの変数をピックアップして散布図とヒストグラム描写#
#**************************************************************************************#
plt.figure(figsize=(10, 6))
plt.scatter(student_merge['G3_math'], student_merge['G3_por'])
plt.grid(True)
plt.show()

plt.hist(student_merge['G3_math'], bins=10)
plt.subplot(1, 2, 2)
plt.hist(student_merge['G3_por'], bins=10)
plt.tight_layout()
plt.show()