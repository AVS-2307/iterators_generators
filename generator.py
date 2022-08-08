nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(_list):
    main_cursor = 0
    nest_cursor = - 1
    while main_cursor < len(_list):
        while nest_cursor < len(_list[main_cursor]) - 1:
            nest_cursor += 1
            yield _list[main_cursor][nest_cursor]
        main_cursor += 1
        nest_cursor = -1



