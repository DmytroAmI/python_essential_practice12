"""
Builder pattern
Builder — це креативний шаблон проектування,
який дозволяє поетапно будувати складні об’єкти.
"""


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_cost(self):
        return sum(item.price for item in self.items)


class OrderBuild:
    def __init__(self):
        self.order = Order()

    def add_item(self, item):
        self.order.add_item(item)
        return self

    def build(self):
        return self.order


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


item1 = Item("Banana", 100)
item2 = Item("Orange", 200)
item3 = Item("Plum", 50)
builder = OrderBuild()
order = builder.add_item(item1).add_item(item2).add_item(item3).build()
print(order.total_cost())
