# Словарь
print('D I C T')
my_dict = {'milk':59, 'sugar':68, 'bread':45} #прайс цен
print(my_dict)
print(my_dict.get('milk'))  #вывод значения ключа
print(my_dict.get('kaffee'))
my_dict['kaffee']=200  # добавление пары
my_dict['egg']=100     # ключ:значение
a=my_dict.pop('sugar')   # удаление пары ключ:значение
print(a)
print(my_dict)

# Множество
print('S E T')
my_set={1,2,4,6,(1,2,3,1),7,3,4,5,False,'end'}
print(my_set)
my_set.add(8)           #добавление элемента
my_set.add('home')      #добавление элемента
print(my_set)
my_set.discard(1)       #удаление элемента
my_set.discard('end')   #удаление элемента
print(my_set)

