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
