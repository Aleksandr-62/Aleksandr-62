first = input('Введите 1-е число:')
second = input('Ведите 2-е число:')
third =  input('Ведите 3-е число:')
if first == second and first == third and second == third:
    print("3")
elif first != second and first != third and second != third:
    print("0")
else:
    print ('2')
