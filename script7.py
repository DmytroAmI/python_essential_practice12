"""
Pattern Adapter
Адаптер — це структурний патерн проектування,
що дає змогу об’єктам із несумісними інтерфейсами працювати разом.
"""


class Adaptee:
    def specific_request(self):
        return "Specific Request"


class Target:
    def request(self):
        return "Standard Request"


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"


adaptee1 = Adaptee()
adapter1 = Adapter(adaptee1)
print(adapter1.request())
