from random import randint


def find_pairs(numbers):
    pairs = []
    for i in range(1, numbers):
        for j in range(i + 1, numbers):
            if (i + j) % numbers == 0:
                pairs.append((i, j))

    return pairs


while True:
    numbers = randint(3, 20)
    print(f"Число: {numbers}")
    pairs = find_pairs(numbers)
    if pairs:
        for item in pairs:
            for number in item:

                print(number, end="")
        break
    else:
        print("Нет пар чисел, кратных сумме")
