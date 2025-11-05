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
#総合1 0~1の値を取る乱数を２組作成．                                                  #
#*************************************************************************************#
random_dataX = np.random.uniform(0.0, 1.0, 10000)
random_dataY = np.random.uniform(0.0, 1.0, 10000)

#*************************************************************************************#
#総合2 (0,0)中心の半径１の円と１の辺を考える．縁の内部に入るのは？                    #
#*************************************************************************************#
inside_circle_x = []
inside_circle_y = []

outside_circle_x = []
outside_circle_y = []

inside_count = 0
for count in range(0, 10000):
    distance = math.hypot(random_dataX[count], random_dataY[count])
    if distance < 1:
        inside_circle_x.append(random_dataX[count])
        inside_circle_y.append(random_dataY[count])
        inside_count = inside_count + 1
    else:
        outside_circle_x.append(random_dataX[count])
        outside_circle_y.append(random_dataY[count])
print(inside_count)

plt.figure(figsize=(10, 6))
circle_x = np.arange(0.0, 1.0, 0.001)
circle_y = np.sqrt(1 - circle_x * circle_x)

plt.plot(circle_x, circle_y)

plt.scatter(inside_circle_x, inside_circle_y, color="r")
plt.scatter(outside_circle_x, outside_circle_y, color="b")

plt.grid(True)

plt.show()

