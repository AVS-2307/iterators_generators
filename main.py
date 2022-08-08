from generator import flat_generator
from iterator import FlatIterator, flatlist_via_comprehension, flatlist_of_different_depth

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list_deep = [
    ['a', 'b', 'c', ['f', [None]]],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None, ['gfr', None, [1, 323, 'ytreef']]],
]

if __name__ == '__main__':
    # for i in FlatIterator(nested_list):
    #     print(i)

    # flatlist_via_comprehension(nested_list)
    # flatlist_of_different_depth(nested_list_deep)

    for i in flat_generator(nested_list_deep):
        print(i)



