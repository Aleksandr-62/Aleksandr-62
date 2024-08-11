immutable_var=1, 2, 3, 4, True # кортетж
print(immutable_var)
#immutable_var [0] = (another)
#immutable_var [0] = (5)
    # В кортедже элементы изменить нельзя!
    #=>TypeError: 'tuple' object does not support item assignment
mutable_list = ['milk', 'sugar', 'bread'] #список
print(mutable_list)
mutable_list [0]='koffee' # изменение элемнта
mutable_list [1]=100      # списка
print(mutable_list)