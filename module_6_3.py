class Horse:
    """
    Класс описывающий лошадь
    """
    x_distance = 0  # пройденный путь.
    sound = 'Frrr'  # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    """
    Класс описывающий орла
    """
    y_distance = 0  # высота полёта
    _sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл(отсылка)

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    """
    Класс наследник Horse, Eagle - описывает мифического пегаса.
    """
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def __init__(self):
        self.sound = super().sound
        self.sound = super()._sound  # передает звук Eagle

    def voice(self):
        print(self.sound)
        return self.sound


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
