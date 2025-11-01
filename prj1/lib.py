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

#データサイエンスにおいて，与えられたデータの中からランダムなものを
#取り出す作業は良くする．そんな時には random.choice
#２つの１つのオプション→一つ目は捜査対象の配列，２つ目は取り出し数
#オプションはreplaceで，Trueにすると（もしくは省略した時）重複を許す
data = np.array([3, 6, 7, 4,5, 1, 9, 8, 5, 3])
print(random.choice(data, 10))
print(random.choice(data, 10, replace = False))

#numpyは行列計算もできる．arrange関数は指定した連続整数を発生させる．
#arrange(9)とした場合，０から８までの整数を出力する．
np.arange(9)
array1 = np.arange(9).reshape(3,3)
print(array1)
#[0,:]を指定すると，一行目，すべての列という意味で，
array1[0,:]
print(array1[0,:])
#[:,0]を指定すると，一列目．．．
print(array1[:,0])
#43ページまでやった
 
 #fuu...fuu.

 #のどが痛い．．．
 #のどが痛いのが治った！＠
#行列の計算
#3 x 3の行列を作成し，変数に代入．
array2 = np.arange(9, 18).reshape(3, 3)
print(array2)
#行列の掛け算はdot関数を使う．
np.dot(array1, array2)

#np.zerosとかnp.onesとかで要素が０とか１の行列を作る．
print(np.zeros(2, 3), dtype = np.int64)
print(np.ones(2, 3), dtype = np.float64)

#次は45ページから．

#scipyについて，
#scipyは線形代数用のライブラリ．
import scipy.linalg as linalg
from scipy.optimize import minimize_scalar

#行列式を計算する例 detを使う
matrix = np.array([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
print(linalg.det(matrix))

#逆行列を計算するにはinv関数を使う
print(linalg.inv(matrix))
#元の行列と逆行列の積は単位行列だから．．．
print(matrix.dot(linalg.inv(matrix)))

#固有値と固有ベクトル eig関数
eig_value, eig_vector = linalg.eig(matrix)
#固有値と固有ベクトル
print(eig_value)
print(eig_vector)

#p55までやった


