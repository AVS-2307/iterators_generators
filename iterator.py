from iteration_utilities import deepflatten


class FlatIterator:

    def __init__(self, _list):
        self._list = _list
        self.main_cursor = -1
        self._list_end = len(_list)

    def __iter__(self):
        self.main_cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self._list[self.main_cursor]):
            iter(self)
        if self.main_cursor == self._list_end:
            raise StopIteration
        self.nest_cursor += 1
        return self._list[self.main_cursor][self.nest_cursor - 1]


# flatlist через comprehension
def flatlist_via_comprehension(_list):
    print()
    print('-' * 10, 'flatlist через comprehension в виде списка', '-' * 10)
    print([item for row in _list for item in row], end='')
    print()
    print()
    print('-' * 10, 'вывод каждого элемента flatlist через comprehension', '-' * 10)
    print(*[item for row in _list for item in row], end='')
    print()


# обработка списка разной глубины
def flatlist_of_different_depth(_list):
    flat_li = list(deepflatten(_list))
    print()
    print('-' * 10, 'flatlist списка разной глубины', '-' * 10)
    print(*flat_li, end='')
    print()
    print()
