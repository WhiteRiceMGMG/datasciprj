import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#np.set_printoptions(precision=3, suppress=True)

#numpyについて
data = np.array([9, 3, 5, 1, 2, 6, 8, 7, 4])
print(data)
#型確認
print(data.dtype)
#次元数確認
print(data.ndim)
#要素数確認
print(data.size)
#すべての要素を2倍にする．
print(data * 2)
#リストをそのまままるっとかけざんみたいなのもできる 
data2 = np.array([9, 3, 5, 1, 2, 6, 8, 7, 4]) * np.array([9, 3, 5, 1, 2, 6, 8, 7, 4])
print(data2)

