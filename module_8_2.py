# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:  # подсчет количества выявленных ошибок типов данных
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return (result, incorrect_data)  # возврат полученных результатов в виде кортежа


def calculate_average(numbers):
    try:
        per_sum = personal_sum(numbers)
        avg = per_sum[0] / (len(numbers) - per_sum[1])
        return avg
    except ZeroDivisionError:  # исключение ошибок деления на 0
        return 0
    except TypeError:  # исключение ошибок типа данных
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать