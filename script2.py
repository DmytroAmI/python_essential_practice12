"""
Singleton — це креативний шаблон проектування,
який гарантує існування лише одного об’єкта такого типу
та забезпечує єдину точку доступу до нього для будь-якого іншого коду.
"""


class DataBaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
