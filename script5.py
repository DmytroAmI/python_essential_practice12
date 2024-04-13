"""
Pattern decorator
class decorator
"""


class Coffee:
    @staticmethod
    def cost():
        return 10


class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self): return self.coffee.cost() + 4


class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self): return self.coffee.cost() + 3


coffee1 = Coffee()
coffee_with_milk_and_sugar = MilkDecorator(SugarDecorator(coffee1))
print(coffee_with_milk_and_sugar.cost())
