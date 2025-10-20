print('hello')
########################################################
# テスト用                                             #
########################################################
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data_list)
print(data_list[3])


print(data_list * 2)

dic_data = {
    'apple'  : 100, 
    'banana' : 200,
    'orange' : 300
}
print(dic_data['apple'])

dummy_val = 2
if dummy_val in data_list :
    print('{0}は入っています'.format(dummy_val))
else :
    print('{0}は入っていません'.format(dummy_val))

total = 0

#リストをforで回すときは単純に配列取っていく＞＞＞？
for temp_num in [1,2,3]:
    print('temp_num:',temp_num)
    total = total + temp_num

print('total:', total)

#辞書をforで回すときはキーの方を入れる＞＞＞？
for dic_key in dic_data:
    print(dic_key, dic_data[dic_key])

#rangeで連続地を取れる＞＞＞？
for temp in range(10):
    print(temp)

#rangeは飛び値もできる＞？
for temp in range(1,11,2):
    print(temp)

#キーと値を同時に取り出すんやが，items()関数が使える
for key, value in dic_data.items():
    print(key, value)

#内包for 
data_list2 = []
data_list2 = [temp * 2 for temp in data_list]
print(data_list2)

#zip関数
for one, two in zip([1, 






2, 3], [4, 5, 6]):
    print(one, two)

#while
temp_num  = 1
while temp_num <= 10:
    print(temp_num)
    temp_num = temp_num + 1
print(temp_num)

#関数
def calc_multi(a,b):
    return a * b

print(calc_multi(2,3))

#無名関数とmap

def calc_calc(a,b):
    return a * b

#これは次のように書ける
(lambda a, b: a * b)(3, 10)
print((lambda a, b: a * b)(3, 10))

#要素に対して何か処理したいときはmap関数を使う
def calc_double(a):
    return a * 2

for num in [1, 2, 3, 4]:
    print(calc_double(num))

#map関数を使うと．．．
#mapはリスト型を帰さず，イテレータを帰すため，
#明示的にlistに変換する．
print(list(map(calc_double, [1, 2, 3, 4])))

#map関数とlabmda関数を組み合わせて．．．




