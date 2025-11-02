import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

student_data_math = pd.read_csv('chap3/student-mat.csv', sep=';')
#print(student_data_math.head(10))

print(student_data_math.info())




