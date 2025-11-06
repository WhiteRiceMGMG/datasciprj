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
print(student_por_data['absences'].descrive())

#*************************************************************************************#
#3-2 数学のデータとポルトガル語のデータをマージ．                                     #
# ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Menu', 'Fedu', 'Mjob',   #
#  'Fjob', 'reason', 'nursery', 'internet']                                           #
# suffixes=('_math', '_por')                                                          #
#*************************************************************************************#


