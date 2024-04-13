"""
Observer pattern
Спостерігач — це поведінковий шаблон проектування,
який дозволяє деяким об’єктам повідомляти інші об’єкти про зміни у своєму стані.
"""


class Subject:
    def __init__(self):
        self._observer = []

    def attach(self, observer):
        self._observer.append(observer)

    def notify(self, message):
        for observer in self._observer:
            observer.update(message)


class Observer:
    @staticmethod
    def update(message):
        print(message)


subject = Subject()
observer1 = Observer()
observer2 = Observer()
observer3 = Observer()
subject.attach(observer1)
subject.attach(observer1)
subject.attach(observer1)
subject.notify("Hello observers")
