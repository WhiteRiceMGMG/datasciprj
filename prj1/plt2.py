import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#シード値の指定
np.random.seed(0)

#データの範囲
numpy_data_x = np.arange(1000)

#乱数の発生と積み上げ
numpy_random_data_y = np.random.randn(1000).cumsum()

#グラフの大きさを指定
plt.figure(figsize = (20, 6))

#label = 1とlegendでラベルを付けることが可能
plt.plot(numpy_data_x, numpy_random_data_y, label='Label')
plt.legend()

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()