"""
Іноді коли клас має один метод
та не не має додаткового функціоналу,
простіше замість класу реалізувати метод.
Дивитись по ситуації.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r1 = Rectangle(2, 4)
print(r1.area())
