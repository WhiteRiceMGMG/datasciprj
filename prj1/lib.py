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

#ソートもできる！data が完全に置き換わってしまうのに注意．
data.sort()
print(data)

#大きい順にするにはソート機能を使うが，，，
#data[::-1].sort()のように操作する．
#[n:m:s]のように書くと，n番目からm-1番目までをsずつ取り出す．
#n やmを飛ばすと，すべてという意味になる．
data[::-1].sort()
print(data)
#p38までやった．


#最小，最大，合計，積み上げの計算
#cumsum→前から順に積み上げていく計算．
print(data.min())
print(data.max())
print(data.sum())
print(data.cumsum())
print(data.cumsum() / data.sum())

#乱数 
import numpy.random as ramdom
#乱数シードの発生
ramdom.seed(0)
#平均０，標準偏差１の正規分布の乱数を取得 randn
random.seed(0)
ran_data = random.randn(10)
print(ran_data)
#ほかにも色々ならんすうの 機能がある．

