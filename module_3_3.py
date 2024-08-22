#Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 2)
print_params(a = '111',b = 111, c = [1,1,1])
print_params(3, 5, 7)
print_params(c = 7, b = 5, a = 3)
print_params(2, 34, c = 3)
print_params(b = 25)
print_params(c = [1,2,3])
print('_______________________________________')
print('# Распаковка')
values_list = [123, 'abc', 1]
values_dict = {'a':2, 'b':'Text', 'c':False}
values_dict1 = {'b':'это', 'c':'Да!', 'a':'Вот'}
print_params(*values_list)
print_params(**values_dict)
print_params(**values_dict1)
print('_______________________________________')
print('#Распаковка + отдельные параметры')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
