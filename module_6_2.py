class Vehicle:
    __COLOR_VARIANTS = ['blue', 'light blue', 'silver', 'grey', 'black', 'dark red']  # Текущие цвета

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner  # владелец (может меняться)
        self.__model = model  # модель транспорта (не меняется)
        self.__engine_power = engine_power  # мощность двигателя (не меняется)
        self.__color = color  # название цвета

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power} л.с.'
              f'\nЦвет: {self.__color}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Невозможно покрасить в {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # (в седан может поместиться только 5 пассажиров)


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()