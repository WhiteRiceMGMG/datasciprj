import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#グラフの大きさを指定
plt.figure(figsize = (20, 6))

#2行1列のグラフの一つ目
plt.subplot(2, 1, 1)

x = np.linspace(-10, 10, 100)
plt.plot(x, np.sin(x))

#2行1列のグラフの2つ目
plt.subplot(2, 1, 2)
y = np.linspace(-10, 10, 1000)
plt.plot(y, np.sin(2 * y))

plt.grid(True)

plt.show()