import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
#シード値の固定
random.seed(0)

#x軸のデータ
x = np.random.randn(30)

#y軸のデータ
y = np.sin(x) + np.random.randn(30)

#グラフの大きさ指定
plt.figure(figsize = (20, 6))

#グラフの描写
plt.plot(x, y, 'o')

plt.scatter(x, y)

plt.title('title name')

plt.xlabel('x')

plt.ylabel('y')

plt.grid(True)

plt.show()