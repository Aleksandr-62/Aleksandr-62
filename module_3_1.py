calls = 0 # глобальное пространство


def cound_calls():  # счетчик вызовов
    global calls
    calls += 1


def string_info(string):  # информация о строке
    cound_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string_info, list_to_search):  # содержит запись (да/нет)
    cound_calls()
    return string_info.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
