import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#シードの固定
random.seed(0)

#グラフの大きさの指定
plt.figure(figsize = (10, 6))

#ヒストグラムの描写
plt.hist(np.random.randn(10 ** 5) * 10 + 50, bins = 60, range = (20, 80))

plt.grid(True)

plt.show()
