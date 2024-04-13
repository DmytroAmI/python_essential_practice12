"""
Strategy pattern
"""


class SortStrategy:
    def sort(self, dataset):
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset):
        print("Bubble Sort")
        n = len(dataset)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if dataset[j] > dataset[j + 1]:
                    dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]


class QuickSortStrategy(SortStrategy):
    def sort(self, dataset):
        print("Quick Sort")
        self._quick_sort(dataset, 0, len(dataset) - 1)

    def _quick_sort(self, dataset, low, high):
        if low < high:
            pivot_index = self._partition(dataset, low, high)
            self._quick_sort(dataset, low, pivot_index - 1)
            self._quick_sort(dataset, pivot_index + 1, high)

    @staticmethod
    def _partition(dataset, low, high):
        pivot = dataset[high]
        i = low - 1
        for j in range(low, high):
            if dataset[j] <= pivot:
                i += 1
                dataset[i], dataset[j] = dataset[j], dataset[i]
        dataset[i + 1], dataset[high] = dataset[high], dataset[i + 1]
        return i + 1


class Sorter:
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy

    def sort(self, dataset):
        self.sort_strategy.sort(dataset)


data1 = [12, 2, 3, 45, 0, 11, 7, 34]
data2 = [9, 34, 123, 10000, 34, 4, 6, 11]
buble_sorter = Sorter(BubbleSortStrategy())
quick_sorter = Sorter(QuickSortStrategy())

buble_sorter.sort(data1)
print(data1)

quick_sorter.sort(data2)
print(data2)
