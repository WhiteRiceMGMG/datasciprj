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

#********************************************************************************#
#2-1 1から50までの自然数の和．np.arrayで1から50までの配列を作り，総和を求める    #
#********************************************************************************#
natural_array = np.arange(1,51)
print(natural_array.sum())

#********************************************************************************#
#2-2 標準正規分布に従う乱数を１０個発生させる．また，最小値，最大値，合計を求める#
#********************************************************************************#
random.seed(0)
random_data = random.randn(10)
print('min:', random_data.min())
print('max:', random_data.max())
print('sum:', random_data.sum())

#*****************************************************************#
#2-3 要素がすべて3の5x5の行列を作成し，その行列を2乗する計算を実施#
#*****************************************************************#
three_array = 3 * np.ones((5,5), dtype = np.float64)
three_array = three_array ** 2
print(three_array)

#************************************************************#
#2-4 次の行列式を求める. [[1,2,3],[1,3,2],[3,1,2]]           #
#************************************************************#
matrix = np.array([[1,2,3],[1,3,2],[3,1,2]])
matrix_det = linalg.det(matrix)
print(matrix_det)

#************************************************************#
#2-5 上の行列について，逆行列と固有値と固有ベクトルを求める  #
#************************************************************#
matrix_inv = linalg.inv(matrix)
eig_value, eig_vector = linalg.eig(matrix)
print(matrix_inv)
print(eig_value)
print(eig_vector)

#******************************************************************#
#2-6 次の関数の解をニュートン法で求める． f(x) = x ** 3 + 2 * x + 1#
#******************************************************************#
def function(x):
    return (x ** 3 + 2 * x + 1)

print(newton(function,0))

#*********************************************************************#
#2-7 以下のデータでmoneyが400以上の人を絞り込んで，レコードを表示する #
#*********************************************************************#
attri_datal = {'ID'   :['1','2','3','4','5'],
               'SEX'  :['F','M','F','M','F'],
               'MONEY':['1000','2000','500','300','700'],
               'NAME' :['Saito','Horie','Kondo','Kawada','Matsubara']}
attri_data_frame1 = DataFrame(attri_datal)
#型変換
attri_data_frame1['MONEY'] = attri_data_frame1['MONEY'].astype(int)
attri_data_frame2 = attri_data_frame1['MONEY'] >= 500

#************************************************************#
#2-8 2-7のデータに対して，男女別の平均moneyを求めてください．#
#************************************************************#
attri_data_frame1['MONEY'] = attri_data_frame1['MONEY'].astype(int)

female_data = attri_data_frame1[attri_data_frame1['SEX'] == 'F']
male_data   = attri_data_frame1[attri_data_frame1['SEX'] == 'M']

average_money_female = female_data['MONEY'].mean()
average_money_male   = male_data['MONEY'].mean()

print(average_money_female)
print(average_money_male)

#*************************************************************************************#
#2-9 2-7のデータに対して，IDをキーとしてマージする．MoneyとMathとEnglishの平均を求める#
#*************************************************************************************#
