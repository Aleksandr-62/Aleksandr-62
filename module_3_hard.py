#  функция подсчёта данных строк и чисел
def calculate_structure_sum(data_structure):
    summa = 0
    # summa ключей и значений
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
            # сумма (список, кортеж, множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
            # сумма (целых чисел и чисел с плавающей запятой)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
        # сумма (символов в строке)
    elif isinstance(data_structure, str):
        summa += len(data_structure)
        # возврат из функции значения summa
    return summa

# данные из задания
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# вывод результата программы
result = calculate_structure_sum(data_structure)
print(result)
